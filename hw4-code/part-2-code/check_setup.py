#!/usr/bin/env python3
"""Quick script to verify the setup before training"""
import os
import sys

print("=== Checking Setup ===\n")

# Check current directory
print(f"Current directory: {os.getcwd()}\n")

# Check for data files
data_folder = 'data'
required_files = ['train.nl', 'train.sql', 'dev.nl', 'dev.sql', 'test.nl']

print(f"Checking for data files in '{data_folder}/':")
all_found = True
for filename in required_files:
    filepath = os.path.join(data_folder, filename)
    exists = os.path.exists(filepath)
    status = "✓" if exists else "✗"
    print(f"  {status} {filename}")
    if not exists:
        all_found = False

if not all_found:
    print("\n⚠️  Some data files are missing!")
    sys.exit(1)

# Check for required Python files
print("\nChecking for Python files:")
required_py = ['load_data.py', 'train_t5.py', 't5_utils.py', 'utils.py']
for filename in required_py:
    exists = os.path.exists(filename)
    status = "✓" if exists else "✗"
    print(f"  {status} {filename}")

# Check if CUDA is available
import torch
print(f"\nPyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"CUDA device: {torch.cuda.get_device_name(0)}")
    print(f"CUDA version: {torch.version.cuda}")

print("\n✓ Setup looks good! Ready to train.")
print("\nRecommended training command:")
print("python train_t5.py --finetune --learning_rate 1e-3 --scheduler_type cosine --num_warmup_epochs 2 --max_n_epochs 20 --patience_epochs 5 --batch_size 32 --test_batch_size 32 --experiment_name ft_experiment")
