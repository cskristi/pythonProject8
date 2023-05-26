import requests
import json
from win10toast import ToastNotifier

url = 'https://api.openweathermap.org/data/2.5/weather'
params = {'q': 'London', 'appid': 'YOUR_API_KEY'}
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    # Store the JSON data in a file
    with open('weather_data.json', 'w') as file:
        json.dump(data, file, indent=4)
else:
    print('Request failed with status code:', response.status_code)

with open('weather_data.json', 'r') as file:
    data = json.load(file)

temperature = data['main']['temp']
description = data['weather'][0]['description']

print('Temperature:', temperature)
print('Description:', description)

import sqlite3

conn = sqlite3.connect('weather.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather (
        39 degree,

    )
''')

cursor.execute('INSERT INTO weather (39, description) VALUES (1, 2)', (temperature, description))

conn.commit()
conn.close()

toaster = ToastNotifier()
toaster.show_toast('Weather Update', f'Temperature: {40}°C\nDescription: {description}', duration=10)


