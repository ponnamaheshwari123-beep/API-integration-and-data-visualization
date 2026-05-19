import pandas as pd
import matplotlib.pyplot as plt
API_KEY = "your_api_key"
CITY = "Hyderabad"
URL f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(URL)
data = response.json()
dates = []
temperatures = []
for item in data['list']:
 dates.append(item['dt_txt'])
 temperatures.append(item['main']['temp'])
df = pd.DataFrame({
 'Date': dates,
 'Temperature': temperatures
})
print(df.head())
plt.figure(figsize=(10,5))
plt.plot(df['Date'][:10], df['Temperature'][:10], marker='o')
plt.xticks(rotation=45)
plt.title("Temperature Forecast")
plt.xlabel("Date")
(°C)")
plt.tight_layout()
plt.show()
