# 14_collections_demo.py
# Level 1 — Topic 14: collections (defaultdict, deque, NamedTuple)

from collections import defaultdict, deque, namedtuple, Counter


# 1. defaultdict — group items without KeyError
grouped = defaultdict(list)
pairs = [
    ("fruit", "apple"),
    ("fruit", "banana"),
    ("veg", "carrot"),
    ("fruit", "orange"),
]
for category, item in pairs:
    grouped[category].append(item)

print("defaultdict result:")
print(dict(grouped))
# {'fruit': ['apple', 'banana', 'orange'], 'veg': ['carrot']}


# 2. deque — efficient sliding window / queue
print("\ndeque sliding window (maxlen=3):")
window = deque(maxlen=3)
for x in [10, 20, 30, 40, 50]:
    window.append(x)
    print(list(window))


# 3. NamedTuple — lightweight immutable record
Sample = namedtuple("Sample", ["features", "label"])
s = Sample(features=[1.2, 3.4], label="positive")
print("\nNamedTuple:")
print(s.features, s.label)
print(s._asdict())


# 4. Counter
print("\nCounter most common:")
print(Counter("abracadabra").most_common(3))
