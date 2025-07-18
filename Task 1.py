import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Replace with your OpenWeatherMap API key
API_KEY = '5438c392c23350577ab91a7330cc1f24'
CITY = 'London'

# Fetch weather forecast (3-hour intervals for 5 days)
url = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'
response = requests.get(url)
data = response.json()

# Extract temperature and time
times = []
temps = []

for item in data['list']:
    time = item['dt_txt']
    temp = item['main']['temp']
    times.append(datetime.strptime(time, '%Y-%m-%d %H:%M:%S'))
    temps.append(temp)

# Plotting
plt.plot(times, temps, marker='o')
plt.title(f'{CITY} Temperature Forecast')
plt.xlabel('Date & Time')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
