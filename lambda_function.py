
items = [
    ("product1", 70),
    ("product2", 11),
    ("product3", 26),

]


# def sort_item(item):
#     return item[1]


items.sort(key=lambda item: item[1])
print(items)
