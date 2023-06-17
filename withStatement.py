try:
    with open("app.py") as file,
        print("File opened.")
        file.__enter
    age = int(input("Age:"))
    age = int(input("Age: "))
    xfactor = 10/age

except (ValueError, ZeroDivisonError):
    print('You didnt enter a valid age.')
except ZeroDivisionError:
    print("you didnt enter a valid age.")
else:
    print("no exceptions were thrown.")

