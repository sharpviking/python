items = [
    ("product1", 12),
    ("product2", 11),
    ("product3", 26),
]


filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
