import requests 
import pandas as pd  
import matplotlib.pyplot as plt  

# 1. API Key and Cities List
API_KEY = "d94238ed7964bac03af5eda1a6c9cf0c" 
cities = ["New York", "London", "Tokyo", "Mumbai", "Sydney"]

# 2. Function to Get Weather Data
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "City": city,
            "Temperature": data["main"]["temp"],
            "Weather": data["weather"][0]["description"],
            "Humidity": data["main"]["humidity"]
        }
    else:
        print(f"Could not get data for {city}")
        return None

# 3. Get Weather Data for All Cities
weather_data = []
for city in cities:
    data = get_weather(city)
    if data:
        weather_data.append(data)

# 4. Create a Table using Pandas
df = pd.DataFrame(weather_data)
print("\nWeather Data Table:\n", df)

# 5. Plot Bar Chart for Temperatures
plt.bar(df["City"], df["Temperature"], color="skyblue")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.title("Current Temperatures in Cities")
plt.show()

# 6. Find Hottest and Coldest Cities
hottest = df.loc[df["Temperature"].idxmax()]
coldest = df.loc[df["Temperature"].idxmin()]
print(f"\nHottest city: {hottest['City']} ({hottest['Temperature']}°C)")
print(f"Coldest city: {coldest['City']} ({coldest['Temperature']}°C)")
