#collect user preferences
#-lenght
#-contain upper
#-contain lower
#-contain digits

# get all avaliable character
# random pick character up to lenght
# ensure we have at lest one of each
# ensure lenght is valid

import random
import string

def generate_pass():
    length = int(input("Enter the desired password lenght: ").strip())
    add_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower()
    add_special = input("Include special letters? (yes/no): ").strip().lower()
    add_digits = input("Include digits letters? (yes/no): ").strip().lower()

    if length < 4:
        print("Password length must be at least 4 characters")
        return

    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if add_uppercase == "yes" else ""
    special = string.punctuation if add_special == "yes" else ""
    digits = string.digits if add_digits == "yes" else ""
    all_character = lower + uppercase + special + digits

    required_cha = []
    if uppercase == "yes":
        required_cha.append(random.choice(uppercase))
    if special == "yes":
        required_cha.append(random.choice(special))
    if digits == "yes":
        required_cha.append(random.choice(digits))

    remaining_length = length - len(required_cha)
    password = required_cha

    for _ in range(remaining_length):
        character = random.choice(all_character)
        password.append(character)

    random.shuffle(password)
    myString = "".join(password)

    return myString

password = generate_pass()
print(password)
