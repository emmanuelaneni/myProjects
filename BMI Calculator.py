# BMI Calculator - this will calculate in Kilograms and Pounds
prompt = "Welcome to BMI checker\n"
prompt += "Calculated in this format -->kilograms for weight and meters for height(meters)<--\n"
print(prompt)

def bmi_kilograms(name, weight, height):
    result = weight / (height * height)
    if result < 18.5:
        print(f"{name} is Underweight\n")
    elif result > 18.5 and result < 24.9:
        print(f"{name} is Normal weight\n")
    elif result > 25 and result < 29.9:
        print(f"{name} is Overweight\n")
    else:
        print(f"{name} is Obese\n")


def main():
    while True:
        start = input("Calculate your BMI yes/no: ").lower()
        if start == "yes":
            try:
                name = input("Enter your name: ").title()
                weight = float(input("Weight: ")) 
                height = float(input("Height in (meters): "))
                bmi_kilograms(name=name, weight=weight, height=height)
            except ValueError:
                print("Invalid input. Try again\n")
        elif start == "no":
            print("Thank you, Goodbye...")
            break
        else:
            print("Input not recognised. Try again\n")

main()


