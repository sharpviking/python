items = [
    ("product1", 12),
    ("product2", 11),
    ("product3", 26),
]

prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]

filtered = list(filter(lambda item: item[1] >= 10, items))
filtered = [item for item in items if item[1] >= 10]
