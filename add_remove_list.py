letters = ["a", "b", "c", "d"]


# Add

letters.append("e")
letters.insert(0, "_")

print(letters)
# Remove
letters.pop()

letters.remove("b")
del letters[0]
del letters[0:3]
letters.clear()
print(letters)
