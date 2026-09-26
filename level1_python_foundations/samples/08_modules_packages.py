# 08_modules_packages.py
# Level 1 — Topic 8: Modules, packages, venv, pip / uv
#
# This file demonstrates the idea. For the real package exercise:
#   1. Create folder myutils/
#   2. Put math_helpers.py and __init__.py inside it
#   3. Import from it as shown below

def clamp(value: float, min_val: float, max_val: float) -> float:
    """Clamp a value between min_val and max_val."""
    return max(min_val, min(value, max_val))


if __name__ == "__main__":
    print("clamp(15, 0, 10) →", clamp(15, 0, 10))   # 10
    print("clamp(-5, 0, 10) →", clamp(-5, 0, 10))   # 0
    print("clamp(7, 0, 10)  →", clamp(7, 0, 10))    # 7

    print("\n--- Recommended terminal commands ---")
    print("python -m venv .venv")
    print("# Windows:   .venv\\Scripts\\activate")
    print("# macOS/Linux: source .venv/bin/activate")
    print("pip install --upgrade pip")
    print("pip install requests pandas")
    print("pip freeze > requirements.txt")
    print("\n# Or with uv (faster):")
    print("# uv venv && source .venv/bin/activate")
    print("# uv pip install requests pandas")
