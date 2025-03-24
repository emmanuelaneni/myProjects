# Weight convertor

def kg_to_ibs(user,):
    pound = 2.20462
    result = user * pounds
    return f"{result} pounds"

def ibs_to_kg(user):
    kilogram = 0.453592
    result =user * kilogram
    return f"{result} kg"

def ibs_to_stone(user):
    stones = 14
    result = user / stones
    return f"{result} stones"

def kg_to_stone(user):
    stones = 0.157473
    result = user * stones
    return f"{result} stones"

def stone_to_kg(user):
    kilogram = 6.35
    result = user * kilogram
    return f"{result} kg"

def stone_to_ibs(user):
    pounds = 14
    result = user * pounds
    return f"{result} pounds"

prompt = """
1) kg to ibs.
2) ibs to kg.
3) ibs to stones.
4) kg to stones.
5) stones to kg.
6) stones to ibs.
Enter "quit" to end program.    
"""
# print(prompt)

def main():
    try:
        start = input("Covert your weight yes/no: ").lower()
        if start == "no":
            print("Goodbye...")
        elif start != "yes" and start != "no":
            print("Make up your mind.")
        else:
            if start == "yes":
                user_weight = float(input("Enter your weight in your preferred class (kg,ibs,stones): "))
                user_input = input("Enter a number 1 to 6 or 'quit': ").lower()
                if user_input == "1":
                    print(kg_to_ibs(user_weight))
                elif user_input == "2":
                    print(ibs_to_kg(user_weight))
                elif user_input == "3":
                    print(ibs_to_stone(user_weight))
                elif user_input == "4":
                    print(kg_to_stone(user_weight))
                elif user_input == "5":
                    print(stone_to_kg(user_weight))
                elif user_input == "6":
                    print(stone_to_ibs(user_weight))
                elif user_input == "quit":
                    print("Goodbye")
                else:
                    print("Value not recognised")
    except ValueError:
        print("Invalid entry has been made....")

main()
