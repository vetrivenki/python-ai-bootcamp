# 09_reproducibility.py
# Level 1 — Topic 9: Reproducibility (seeds, pinned environments, uv)

import random

try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False
    print("NumPy not installed — skipping NumPy seed demo.")
    print("Install with: pip install numpy\n")


def set_seed(seed: int = 42):
    """Set seeds for reproducibility."""
    random.seed(seed)
    if HAS_NUMPY:
        np.random.seed(seed)
    # Later for PyTorch:
    # import torch
    # torch.manual_seed(seed)
    # if torch.cuda.is_available():
    #     torch.cuda.manual_seed_all(seed)


if __name__ == "__main__":
    set_seed(42)
    print("random.random() →", random.random())
    if HAS_NUMPY:
        print("np.random.rand(3) →", np.random.rand(3))

    print("\n--- uv quick start ---")
    print("# curl -LsSf https://astral.sh/uv/install.sh | sh")
    print("# uv venv")
    print("# source .venv/bin/activate")
    print("# uv pip install numpy pandas")
    print("# uv pip freeze > requirements.txt")
