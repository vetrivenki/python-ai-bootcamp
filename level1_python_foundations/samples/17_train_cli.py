# 17_train_cli.py
# Level 1 — Topic 17: Simple CLI with argparse

import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="Tiny training script example — Level 1"
    )
    parser.add_argument(
        "--data", type=Path, required=True,
        help="Path to dataset"
    )
    parser.add_argument(
        "--epochs", type=int, default=10,
        help="Number of epochs"
    )
    parser.add_argument(
        "--batch-size", type=int, default=32,
        help="Batch size"
    )
    parser.add_argument(
        "--lr", type=float, default=1e-3,
        help="Learning rate"
    )
    parser.add_argument(
        "--output", type=Path, default=Path("artifacts"),
        help="Output directory"
    )
    parser.add_argument(
        "--verbose", action="store_true",
        help="Print extra logs"
    )

    args = parser.parse_args()

    print("=== Training Config ===")
    print(f"Data path     : {args.data}")
    print(f"Epochs        : {args.epochs}")
    print(f"Batch size    : {args.batch_size}")
    print(f"Learning rate : {args.lr}")
    print(f"Output dir    : {args.output}")
    print(f"Verbose       : {args.verbose}")

    if args.verbose:
        print("\nStarting fake training loop...")
    print("Done.")


if __name__ == "__main__":
    main()

# Example runs:
# python 17_train_cli.py --data ./data/train.csv
# python 17_train_cli.py --data ./data --epochs 50 --batch-size 64 --lr 0.0005 --verbose
