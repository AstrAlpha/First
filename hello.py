# Ask the user for their name, delete the extra space & Capitilize their name
name = input("What's your name? ").title().strip()
first, last = name.split(" ")

# Say hello to the user
print("hello,", first)
"""
as long as these three double aspostrophy are there these are comments

"""
age = input("how old are you? ")

print("good to hear",first,age, sep=" ")
