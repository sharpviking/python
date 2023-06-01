values = list(range(5))
values[*range(5), *"Hello"]
print(values)


first = {"x": 11}
second = {"x": 26, "y": 12}
combined = {**first, **second, "z": 1}
print(combined)
