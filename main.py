# Connect to an API
import requests
import json

response_API = requests.get('https://www.7timer.info/bin/astro.php?lon=113.2&lat=23.1&ac=0&unit=metric&output=json&tzshift=0')
print(response_API)

# Get the data from the API
data = response_API.text
print(data)

# Parse the data into JSON format
parse_json = json.loads(data)

# Extract the data and put in into a JSON file
with open("weatherData.json", "w") as outfile:
    outfile.write(data)


# https://www.askpython.com/python/examples/pull-data-from-an-api