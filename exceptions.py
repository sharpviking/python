 try:
    file = open("app.py")
    age = int(input("Age:"))
    xfactor = 10/ age
except (valueError, ZeroDivisonError):
    print("You didnt entered a valid age.")
else:
   print("no exception were thrown.")
finally:
    file.close()
