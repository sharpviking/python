try:
    age = int(input("Age:"))
except ValueError as ex:
    print("You didnt enter a valid age.")
else:
    print("No exceptions were thrown.")
print("Execution continues.")
