# Average-Temperature Analyzer

# Add a function named get_average_temperature(weather_data) to the program in the previous practice project. This function should accept a list of the weather data dictionaries described in the previous project and return the average temperature in their 'temp' keys. To calculate the average, add all of the temperature numbers in the dictionaries and divide the result by the number of dictionaries.

# The list passed to get_average_temperature() can contain any number of dictionaries but should always contain at least one. Generate a list of 100 weather dictionaries by calling get_random_weather_data(), then pass this list to get_average_temperature() and print the average it returns.

# Add this new function to your weatherDataGen.py program and save this new program as avgTemp.py.

from weatherData import get_random_weather_data
from weatherData import get_list_weather_data


def get_average_temperature(weatherDataList):
    sum = 0
    for data in weatherDataList:
        sum += data["temp"]
    average = sum / len(weatherDataList)
    return average


def main():
    randomDataList = get_list_weather_data()
    print("The average temperature is:" + str(get_average_temperature(randomDataList)))


main()
