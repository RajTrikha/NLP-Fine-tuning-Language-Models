# DSGA 1011 Assignment 4: Fine-tuning Language Models

This repository contains the implementation for HW4, which focuses on fine-tuning pretrained language models for two tasks: BERT sentiment classification and T5 text-to-SQL generation.

## Results Summary

### Part 1: BERT Sentiment Classification
- **Original Test Accuracy**: 91.948%
- **Transformed Test Accuracy**: 89.54% (with data augmentation)
- **Transformation**: Synonym replacement using NLTK WordNet
- **Data Augmentation**: Applied synonym replacement to training data

### Part 2: T5 Text-to-SQL Generation
- **Dev F1 Score**: 85.53% (exceeds 65% requirement)
- **Test F1 Score**: 85.53%
- **Record EM**: 84.33%
- **SQL Error Rate**: 9.87%
- **Model**: T5-small (google-t5/t5-small) fine-tuned
- **Best Epoch**: 24

## Repository Structure

```
hw4-code/
├── part-1-code/
│   ├── main.py              # BERT training and evaluation
│   ├── utils.py             # Data transformation and augmentation
│   └── requirements.txt     # Dependencies for Part 1
│
├── part-2-code/
│   ├── load_data.py         # T5 dataset and data loading
│   ├── train_t5.py          # T5 training script
│   ├── t5_utils.py          # Model initialization utilities
│   ├── utils.py             # Database evaluation utilities
│   ├── evaluate.py          # Evaluation script
│   └── data/                # Dataset (provided by course)
│       ├── train.nl
│       ├── train.sql
│       ├── dev.nl
│       ├── dev.sql
│       ├── test.nl
│       └── (additional data files)
│
└── README.md                # This file
```

## Setup

### Part 1: BERT Sentiment Classification

1. Install dependencies:
```bash
pip install torch torchvision transformers datasets nltk
```

2. Download NLTK resources (run in Python):
```python
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')
```

3. Run training:
```bash
cd part-1-code
python main.py
```

### Part 2: T5 Text-to-SQL

1. Install dependencies:
```bash
pip install torch transformers datasets tqdm
```

2. Ensure data folder exists with all required files (train.nl, train.sql, dev.nl, dev.sql, test.nl, etc.)

3. Run training (fine-tuning):
```bash
cd part-2-code
python train_t5.py \
  --finetune \
  --learning_rate 1e-3 \
  --scheduler_type cosine \
  --num_warmup_epochs 2 \
  --max_n_epochs 30 \
  --patience_epochs 5 \
  --batch_size 16 \
  --test_batch_size 16 \
  --experiment_name ft_experiment
```

4. Generate test predictions:
```bash
python train_t5.py \
  --finetune \
  --test_only \
  --load_model_path checkpoints/ft_experiments/ft_experiment/best_model \
  --experiment_name ft_experiment
```

## Implementation Details

### Part 1: BERT Fine-tuning
- **Base Model**: `bert-base-uncased`
- **Task**: Binary sentiment classification (SST-2)
- **Transformation**: Synonym replacement for adjectives/adverbs
- **Data Augmentation**: Applied transformation to training data to improve robustness

### Part 2: T5 Fine-tuning
- **Base Model**: `google-t5/t5-small` (60M parameters)
- **Task**: Text-to-SQL generation on ATIS dataset
- **Architecture**: Full fine-tuning (no frozen layers)
- **Key Design Choices**:
  - Task prefix: "translate English to SQL: " (T5 best practice)
  - Teacher forcing with proper decoder input/target alignment
  - Decoder targets padded with -100 for loss calculation
  - Greedy decoding (num_beams=1) for inference
  - Cosine learning rate schedule with 2-epoch warmup
  - Early stopping with patience=5 epochs

### Key Hyperparameters (Part 2)
- **Learning Rate**: 1e-3
- **Optimizer**: AdamW (weight_decay=0)
- **Batch Size**: 16
- **Max Sequence Length**: 512 tokens
- **Scheduler**: Cosine annealing with warmup
- **Loss Function**: CrossEntropyLoss(ignore_index=-100)

## Evaluation Metrics

### Part 1
- **Accuracy**: Percentage of correctly classified examples

### Part 2
- **Record F1**: F1 score between database records from generated SQL vs ground truth
- **Record EM**: Exact match of database records
- **SQL EM**: Exact match of SQL queries (string matching)
- **SQL Error Rate**: Percentage of generated SQL with syntax errors

## Error Analysis (Part 2)

Three main error categories identified:

1. **Complex JOIN Handling** (~3-4% of queries): Model struggles with multi-hop JOIN queries for connecting flights
2. **Aggregation with GROUP BY** (~2-3% of queries): Model sometimes omits GROUP BY clause in aggregate queries
3. **Nested Subquery Complexity** (~4-5% of queries): Model generates invalid or oversimplified nested queries

## Model Checkpoint

The best model checkpoint (epoch 24, 85.53% F1) is available via Google Drive link in the report.

## Citation

If you use this code, please cite the original papers:

```bibtex
@article{raffel2019exploring,
  title={Exploring the limits of transfer learning with a unified text-to-text transformer},
  author={Raffel, Colin and Shazeer, Noam and Roberts, Adam and Lee, Katherine and Narang, Sharan and Matena, Michael and Zhou, Yanqi and Li, Wei and Liu, Peter J},
  journal={arXiv preprint arXiv:1910.10683},
  year={2019}
}

@article{devlin2018bert,
  title={BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding},
  author={Devlin, Jacob and Chang, Ming-Wei and Lee, Kenton and Toutanova, Kristina},
  journal={arXiv preprint arXiv:1810.04805},
  year={2018}
}
```

## License

This code is for educational purposes as part of DSGA 1011 coursework.

## Acknowledgments

- Course staff for providing the assignment framework and evaluation scripts
- Hugging Face for the Transformers library
- Google Research for T5 and BERT pretrained models
