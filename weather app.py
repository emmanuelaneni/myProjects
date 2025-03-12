# we import the request module.
import requests

def get_weather(location):
    # We get our API key 
    api_key = "78a46190f11f69e8dd22720e41a3477e"
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&APPID={api_key}")
    # we use json to unpack the data to a dictionary
    data = response.json()

    # this is to check if the request was a success and to get the info needed.
    try:
        if data["cod"] == 200:
            info = {
                'city': data['name'],
                'country code': data['sys']['country'],
                'weather': data['weather'][0]['main'],
                'temperature': data['main']['temp'],
                'feels like': data['main']['feels_like'],
            }

            for item, value in info.items():
                print(f"{item.title()}: {value}")
            print()

        else:
            print("Error, try again")
    except ValueError:
        print("Enter a valid input...")

# get_weather("london")

def main():
    while True:
        get_info = input("Get weather forecast Yes/No: ").lower()
        if get_info == "yes":
            user_country = input("Enter a valid Country: ")
            get_weather(user_country)
        elif get_info == "no":
            print("Thanks, goodbye!")
            break
        else:
            print("Enter Yes or No...")
        
main()
