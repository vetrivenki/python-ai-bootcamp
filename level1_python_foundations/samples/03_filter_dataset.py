# 03_filter_dataset.py
# Level 1 — Topic 3: Loops and comprehensions

students = [
    {"name": "Alice", "age": 22, "score": 88},
    {"name": "Bob",   "age": 19, "score": 72},
    {"name": "Charlie", "age": 25, "score": 95},
    {"name": "Diana", "age": 20, "score": 61},
    {"name": "Eve",   "age": 23, "score": 79},
]

# Traditional loop
passed = []
for s in students:
    if s["score"] >= 75:
        passed.append(s["name"])
print("Passed (loop):", passed)

# List comprehension
passed_comp = [s["name"] for s in students if s["score"] >= 75]
print("Passed (comprehension):", passed_comp)

# Dict comprehension
high_scores = {s["name"]: s["score"] for s in students if s["score"] >= 80}
print("High scores:", high_scores)

# Average score of students older than 21
older = [s for s in students if s["age"] > 21]
avg = sum(s["score"] for s in older) / len(older)
print(f"Average score (age > 21): {avg:.1f}")
