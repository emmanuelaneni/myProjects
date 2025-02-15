import random

ans = random.randint(1, 15)
count = 0
trigger = True

# Uncomment below to view the answer
print(ans)

# Loop to make sure user enters a valid input
while trigger:
    try:
        user_input = int(input("Guess the number: "))
        print("Number accepted!")
        if user_input > ans:
            print("Number entered is higher")
            count += 1
        elif user_input < ans:
            print("Number enter is lower")
            count += 1
        else:
            print(f"Correct. You got the right number {user_input}.")
            trigger = False

# A conditional statement if user and entered 3 in correct input

        if count == 3:
            print("Game over, You did not guess right.")
            print(f"You tried {count} times")
            break
        else:
            continue
        
    except ValueError:
        print("Enter a valid input.")

