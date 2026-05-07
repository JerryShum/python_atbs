import random

# Write a function named get_random_weather_data() that returns a dictionary of random weather data. The dictionary should have the keys and values in Table 7-1.

# The program should then call this function from a loop 100 times, storing the returned dictionaries in a list. Finally, it should print the list. Save this program in a file named weatherDataGen.py.


def get_random_weather_data():
    randTemp = random.uniform(-50, 50)
    randFeelsLike = randTemp + random.randint(-10, 10)
    randHumidity = random.uniform(0, 100)
    randPressure = random.uniform(990, 1010)

    return {
        "temp": randTemp,
        "feels_like": randFeelsLike,
        "humidity": randHumidity,
        "pressure": randPressure,
    }


def main():
    weatherData = []

    for i in range(100):
        weatherData.append(get_random_weather_data())

    print(weatherData)


main()
