import random
RANGE = 20
guess = None



def compare(num1: int, num2: int):
    return (num1 < num2) - (num1 > num2)


while True:
    chosen_number = random.randint(RANGE*-1, RANGE)
    print("The number has been chosen")
    while chosen_number != guess:
        try:
            print(("Correct!\n", "Tip: Too big", "Tipp: Too small")[compare(chosen_number, guess := int(input("Your guess: ")))])
        except ValueError:
            print("Your guess must be an integer")


