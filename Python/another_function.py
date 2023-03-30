def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Abhishek")
file = open("content.txt", "w")
file.write(message)
