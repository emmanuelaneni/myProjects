import random

# The dice function

def diceRoll(number):
    if number <= 0:
        print("Error")
        return ValueError
    
    roll = []
    for x in range(number):
        roll.append(random.randint(1, 6))

    total = sum(roll)
    print(*roll, sep=",")
    print(f"Total dice number = {total}")

# The main function

def main():
    prompt = """\nEnter a number\n"""
    prompt += """Enter exit to terminate program: """
    while True:
        try:
            user = input(prompt).lower()
            if user.isdigit():
                diceRoll(int(user))
            elif user == "exit":
                print("Goodbye")
                break
        except ValueError:
            print("Invalid Input")

main()