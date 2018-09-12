import requests

api_data='https://api.openweathermap.org/data/2.5/weather?appid=f15552cb2204f9027f11e7a8ed4ee806&q='

city=input("Enter your city :")

url=api_data + city
json_data=requests.get(url).json()
print(json_data)