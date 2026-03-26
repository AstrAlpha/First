def greet(user_input):
    if("hello") in user_input:
        print("hello there")
    else:
        print("IDK what you mean")

text = input("Say something: ")
greet(text)

to = input("How are you?")
print(f"{to}")
if("good") in to.lower():
    print("Great!")
else:
    print("May your day be fine!")
