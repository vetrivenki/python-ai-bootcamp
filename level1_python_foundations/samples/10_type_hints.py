# 10_type_hints.py
# Level 1 — Topic 10: Type hints with mypy

from typing import List, Dict, Optional, Union


def average(numbers: List[float]) -> float:
    if not numbers:
        raise ValueError("List cannot be empty")
    return sum(numbers) / len(numbers)


def find_user(users: Dict[str, dict], user_id: str) -> Optional[dict]:
    return users.get(user_id)


def process(value: Union[int, str]) -> str:
    return str(value).upper()


if __name__ == "__main__":
    print(average([10.0, 20.0, 30.0]))
    print(find_user({"u1": {"name": "Alice"}}, "u1"))
    print(process(42))
    print(process("hello"))

    print("\n# To type-check this file:")
    print("# pip install mypy")
    print("# mypy 10_type_hints.py")
