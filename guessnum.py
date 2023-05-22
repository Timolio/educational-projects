import random


RANGE = 5
guess = None
attempt = 0
exp = 0


def compare(num1: int, num2: int):
    return (num1 < num2) - (num1 > num2)


while True:
    exp += (increase := RANGE/20 * (0, 100, 50, 10, 1)[attempt*(lambda x: int(x < 5))(attempt)])
    attempt = 0
    print(f"{exp} XP (+{increase}) with a range of {RANGE}\n")

    chosen_number = random.randint(RANGE*-1, RANGE)
    print("*The number has been chosen*")
    while chosen_number != guess:
        attempt += 1
        try:
            print(("Correct!\n", "Tip: Too big", "Tipp: Too small")[compare(chosen_number, guess := int(input("Your guess: ")))])
        except ValueError:
            print("Your guess must be an integer")


