# NLP Fine-tuning Language Models

**Author:** Raj Trikha (rt2932)

**Best Result:** Achieved the highest F1 score for T5 fine-tuning: **F1 = 79.85**

---

This repository contains implementations for fine-tuning and prompting language models on two NLP tasks:

1. **Sentiment Analysis** - Fine-tuning BERT for IMDB movie review classification
2. **Text-to-SQL** - Converting natural language queries to SQL using T5 fine-tuning and LLM prompting

## Project Structure

```
.
├── part-1-code/          # Sentiment Analysis with BERT
│   ├── main.py           # Training and evaluation pipeline
│   ├── utils.py          # Data augmentation utilities
│   └── requirements.txt
│
└── part-2-code/          # Text-to-SQL Generation
    ├── train_t5.py       # T5 fine-tuning pipeline
    ├── prompting.py      # LLM prompting with Gemma
    ├── evaluate.py       # Evaluation metrics
    ├── load_data.py      # Data loading utilities
    ├── t5_utils.py       # T5 model utilities
    ├── prompting_utils.py
    ├── utils.py
    ├── data/             # Dataset files
    ├── results/          # Generated SQL outputs
    ├── records/          # Database query records
    └── requirements.txt
```

## Part 1: Sentiment Analysis

Fine-tuning BERT (`bert-base-cased`) for binary sentiment classification on the IMDB dataset.

### Features
- Training loop implementation with learning rate scheduling
- Data augmentation for improved robustness
- Evaluation on original and transformed test sets

### Setup

```bash
cd part-1-code
conda create -n nlp-part1 python=3.9
conda activate nlp-part1
pip install -r requirements.txt

# Download NLTK resources
python -c "import nltk; nltk.download('wordnet'); nltk.download('punkt')"
```

### Usage

```bash
# Train on original dataset
python main.py --train --num_epochs 3 --learning_rate 5e-5

# Train with augmented data
python main.py --train_augmented --num_epochs 3

# Evaluate on test set
python main.py --eval --model_dir ./out

# Evaluate on transformed test set
python main.py --eval_transformed --model_dir ./out
```

## Part 2: Text-to-SQL

Converting natural language queries to SQL for a flight database using two approaches:

1. **T5 Fine-tuning** - Training T5 from scratch or fine-tuning pretrained weights
2. **LLM Prompting** - Zero-shot and few-shot prompting with Gemma models

### Setup

```bash
cd part-2-code
conda create -n nlp-part2 python=3.10
conda activate nlp-part2
pip install -r requirements.txt
```

### T5 Training

```bash
# Fine-tune T5
python train_t5.py --finetune --max_n_epochs 20 --learning_rate 1e-4 --batch_size 16

# Train from scratch
python train_t5.py --max_n_epochs 50 --learning_rate 1e-3
```

### LLM Prompting

```bash
# Zero-shot prompting with Gemma
python prompting.py --model gemma --shot 0

# Few-shot prompting
python prompting.py --model gemma --shot 3

# Use CodeGemma with quantization
python prompting.py --model codegemma --shot 3 --quantization
```

### Evaluation

```bash
python evaluate.py \
    --predicted_sql results/t5_ft_dev.sql \
    --predicted_records records/t5_ft_dev.pkl \
    --development_sql data/dev.sql \
    --development_records records/ground_truth_dev.pkl
```

## Requirements

### Part 1
- Python 3.9+
- PyTorch 1.13+
- Transformers 4.26+
- NLTK

### Part 2
- Python 3.10+
- PyTorch 2.1+
- Transformers 4.40+
- Accelerate
- bitsandbytes (for quantization)
- Weights & Biases (optional, for experiment tracking)

## Models Used

- **BERT** (`bert-base-cased`) - Sentiment classification
- **T5** (`t5-small`) - Text-to-SQL generation
- **Gemma** (`google/gemma-1.1-2b-it`) - LLM prompting
- **CodeGemma** (`google/codegemma-7b-it`) - Code-optimized LLM prompting

## License

This project is for educational purposes.
