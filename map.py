items = [
    ("product1", 12),
    ("product2", 11),
    ("product3", 26),
]


# prices = []
# for item in items:
#     prices.append(item[1])

prices = list(map(lambda item: item[1], items))
print(prices)
