# 02_word_counter.py
# Level 1 — Topic 2: Lists, dicts, sets, tuples

from collections import Counter

text = """
Python is great. Python is powerful.
Learning Python with hands-on projects is the best way.
"""

# Clean and split
words = text.lower().replace(".", "").replace(",", "").split()

# Using Counter (dict subclass)
word_counts = Counter(words)

print("Word frequencies:")
for word, count in word_counts.most_common():
    print(f"{word:15} → {count}")

# Unique words (set)
unique_words = set(words)
print(f"\nTotal unique words: {len(unique_words)}")
print(f"Unique words: {sorted(unique_words)}")
