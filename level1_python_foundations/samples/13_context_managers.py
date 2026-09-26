# 13_context_managers.py
# Level 1 — Topic 13: Context managers (with statement)

from contextlib import contextmanager
import time


class Timer:
    """Class-based context manager that measures elapsed time."""

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start
        print(f"Elapsed: {self.elapsed:.4f}s")
        return False  # do not suppress exceptions


@contextmanager
def open_and_count(path: str):
    """Generator-based context manager that opens a file and counts lines."""
    f = open(path, "r", encoding="utf-8")
    try:
        lines = f.readlines()
        yield lines
    finally:
        f.close()
        print(f"Closed {path} ({len(lines)} lines)")


if __name__ == "__main__":
    print("--- Class-based Timer ---")
    with Timer():
        time.sleep(0.2)
        print("Working...")

    print("\n--- Generator-based open_and_count ---")
    with open("demo_lines.txt", "w") as f:
        f.write("line one\nline two\nline three\n")

    with open_and_count("demo_lines.txt") as lines:
        print("Content:", [l.strip() for l in lines])
