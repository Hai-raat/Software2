# Question 1.
import requests
response = requests.get("https://api.chucknorris.io/jokes/random")
data = response.json()
print(data["value"])

# Question 2
import requests
city = input("Enter municipality/city name: ")

api_key = "9b35b4ccf8c833bfcf73918b11346c4a"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]

    print(f"Weather in {city}: {description}")
    print(f"Temperature: {temperature} °C")

else:
    print("Error: Could not get weather data. Check city name or API key.")