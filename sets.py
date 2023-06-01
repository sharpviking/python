numbers = [11, 22, 26, 26, 11, 11]
first = set(numbers)
second = {1, 11}
# second.add(5)
# second.remove(4)
# len(second)
print(first | second)
print(first & second)
print(first-second)
print(first ^ second)

if 11 in first:
    print("yes")
