def main():
    guess = get_guess#
    if guess == 50:
        print("Correct!")
    else:
        print("Incorrect!")


def get_guess():
    guess = int(input("What's your guess?"))
    return guess


get_guess()
main()
