# Dice Simulator
import random

one = """
+---+
| * |
+---+
"""
two = """
+---+
|* *|
+---+
"""
three = """
+---+
|***|
+---+
"""
four = """
+---+
|* *|
|* *|
+---+
"""
five = """
+---+
|***|
|* *|
+---+
"""

six = """
+---+
|***|
|***|
+---+
"""


def diceRoll():
    diceAscii = [one, two, three, four, five, six]
    output = random.randint(1, 6)
    # print(output)
    if output == 1:
        print(diceAscii[0])
    elif output == 2:
        print(diceAscii[1])
    elif output == 3:
        print(diceAscii[2])
    elif output == 4:
        print(diceAscii[3])
    elif output == 5:
        print(diceAscii[4])
    elif output == 6:
        print(diceAscii[5])

# diceRoll()

def main():
    count = 0
    while True:
        user = input("Role the dice Yes or No: ").lower()
        if user == "yes":
            diceRoll()
            count += 1
        elif user == "no":
            print("Goodbye")
            break
        else:
            print("Invalid response")

main()
