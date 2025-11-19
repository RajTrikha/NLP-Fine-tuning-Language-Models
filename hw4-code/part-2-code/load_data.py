import os, random, re, string
from collections import Counter
from tqdm import tqdm
import pickle

from torch.utils.data import Dataset, DataLoader
from torch.nn.utils.rnn import pad_sequence

import nltk
nltk.download('punkt')
from transformers import T5TokenizerFast
import torch

PAD_IDX = 0

class T5Dataset(Dataset):

    def __init__(self, data_folder, split):
        '''
        Dataset class for T5 model.

        Args:
            data_folder: Path to data directory
            split: 'train', 'dev', or 'test'
        '''
        self.split = split
        self.tokenizer = T5TokenizerFast.from_pretrained('google-t5/t5-small')

        # Process data
        self.data = self.process_data(data_folder, split, self.tokenizer)

    def process_data(self, data_folder, split, tokenizer):
        '''
        Load and tokenize data from .nl and .sql files.
        '''
        # Load natural language queries
        nl_path = os.path.join(data_folder, f'{split}.nl')
        with open(nl_path, 'r') as f:
            nl_queries = [line.strip() for line in f.readlines()]

        # Load SQL queries (except for test set)
        if split != 'test':
            sql_path = os.path.join(data_folder, f'{split}.sql')
            with open(sql_path, 'r') as f:
                sql_queries = [line.strip() for line in f.readlines()]
        else:
            sql_queries = None

        # Tokenize
        data = []
        for i, nl_query in enumerate(nl_queries):
            # Add task prefix (T5 best practice from Raffel et al., 2019)
            prefixed_query = "translate English to SQL: " + nl_query

            # Tokenize encoder input (natural language with prefix)
            encoder_input = tokenizer.encode(prefixed_query, add_special_tokens=True, truncation=True, max_length=512)

            if split != 'test':
                # Tokenize SQL query (no modifications)
                sql_query = sql_queries[i]

                # First create decoder target with EOS token
                decoder_target = tokenizer.encode(sql_query, add_special_tokens=True, truncation=True, max_length=512)

                # Ensure EOS token is present (T5 tokenizer sometimes omits it)
                if decoder_target[-1] != tokenizer.eos_token_id:
                    decoder_target.append(tokenizer.eos_token_id)

                # Create decoder input by shifting: prepend PAD, remove last token (EOS)
                # This implements proper teacher forcing
                decoder_input = [tokenizer.pad_token_id] + decoder_target[:-1]

                data.append({
                    'encoder_input': torch.tensor(encoder_input, dtype=torch.long),
                    'decoder_input': torch.tensor(decoder_input, dtype=torch.long),
                    'decoder_target': torch.tensor(decoder_target, dtype=torch.long)
                })
            else:
                # Test set: only encoder input
                data.append({
                    'encoder_input': torch.tensor(encoder_input, dtype=torch.long)
                })

        return data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

def normal_collate_fn(batch):
    '''
    Collation function to perform dynamic padding for training and evaluation with the
    development or validation set.

    Inputs:
        * batch (List[Any]): batch is a list of length batch_size, where each index contains what
                             the dataset __getitem__ function returns.

    Returns: To be compatible with the provided training loop, you should be returning
        * encoder_ids: The input ids of shape BxT to be fed into the T5 encoder.
        * encoder_mask: Mask of shape BxT associated with padding tokens in the encoder input
        * decoder_inputs: Decoder input ids of shape BxT' to be fed into T5 decoder.
        * decoder_targets: The target tokens with which to train the decoder (the tokens following each decoder input)
        * initial_decoder_inputs: The very first input token to be decoder (only to be used in evaluation)
    '''
    # Extract from batch
    encoder_inputs = [item['encoder_input'] for item in batch]
    decoder_inputs = [item['decoder_input'] for item in batch]
    decoder_targets = [item['decoder_target'] for item in batch]

    # Pad sequences
    encoder_ids = pad_sequence(encoder_inputs, batch_first=True, padding_value=PAD_IDX)
    decoder_input_ids = pad_sequence(decoder_inputs, batch_first=True, padding_value=PAD_IDX)
    # Use -100 for decoder targets (PyTorch CrossEntropyLoss ignore_index)
    decoder_target_ids = pad_sequence(decoder_targets, batch_first=True, padding_value=-100)

    # Create attention mask for encoder (1 for real tokens, 0 for padding)
    encoder_mask = (encoder_ids != PAD_IDX).long()

    # Initial decoder input (just the BOS token)
    initial_decoder_inputs = decoder_input_ids[:, 0:1]  # Shape: (B, 1)

    return encoder_ids, encoder_mask, decoder_input_ids, decoder_target_ids, initial_decoder_inputs

def test_collate_fn(batch):
    '''
    Collation function to perform dynamic padding for inference on the test set.

    Inputs:
        * batch (List[Any]): batch is a list of length batch_size, where each index contains what
                             the dataset __getitem__ function returns.

    Recommended returns:
        * encoder_ids: The input ids of shape BxT to be fed into the T5 encoder.
        * encoder_mask: Mask of shape BxT associated with padding tokens in the encoder input
        * initial_decoder_inputs: The very first input token to be decoder (only to be used in evaluation)
    '''
    # Extract encoder inputs
    encoder_inputs = [item['encoder_input'] for item in batch]

    # Pad sequences
    encoder_ids = pad_sequence(encoder_inputs, batch_first=True, padding_value=PAD_IDX)

    # Create attention mask
    encoder_mask = (encoder_ids != PAD_IDX).long()

    # Initial decoder input (BOS token = pad_token_id for T5)
    batch_size = encoder_ids.size(0)
    initial_decoder_inputs = torch.full((batch_size, 1), PAD_IDX, dtype=torch.long)

    return encoder_ids, encoder_mask, initial_decoder_inputs

def get_dataloader(batch_size, split):
    # Find data folder - check multiple possible locations
    possible_paths = [
        'data',  # Same directory
        '../data',  # Parent directory
        os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')  # Two levels up from this file
    ]

    data_folder = None
    for path in possible_paths:
        test_file = os.path.join(path, f'{split}.nl')
        if os.path.exists(test_file):
            data_folder = path
            break

    if data_folder is None:
        raise FileNotFoundError(f"Could not find data folder. Searched: {possible_paths}")

    dset = T5Dataset(data_folder, split)
    shuffle = split == "train"
    collate_fn = normal_collate_fn if split != "test" else test_collate_fn

    dataloader = DataLoader(dset, batch_size=batch_size, shuffle=shuffle, collate_fn=collate_fn)
    return dataloader

def load_t5_data(batch_size, test_batch_size):
    train_loader = get_dataloader(batch_size, "train")
    dev_loader = get_dataloader(test_batch_size, "dev")
    test_loader = get_dataloader(test_batch_size, "test")
    
    return train_loader, dev_loader, test_loader


def load_lines(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines

def load_prompting_data(data_folder):
    # For prompting approaches (not needed for this assignment)
    train_x = load_lines(os.path.join(data_folder, 'train.nl'))
    train_y = load_lines(os.path.join(data_folder, 'train.sql'))
    dev_x = load_lines(os.path.join(data_folder, 'dev.nl'))
    dev_y = load_lines(os.path.join(data_folder, 'dev.sql'))
    test_x = load_lines(os.path.join(data_folder, 'test.nl'))

    return train_x, train_y, dev_x, dev_y, test_x