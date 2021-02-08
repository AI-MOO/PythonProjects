import requests
def city_weather():
    city = input("please enter your city to get the weather: ")

    # API call : api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
    # API key : f961de08056332095ab66a5e8cdae23e
    API = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=f961de08056332095ab66a5e8cdae23e".format(city)
    weather_data = requests.get(API).json()

    # print all weahter inforamtion:
    print(weather_data)                             # json data

    # print particular information:
    print("=============================================")
    main_weather = weather_data['weather'][0]['main']
    description = weather_data['weather'][0]['description']
    temperature = weather_data['main']['temp']

    print('main_weather: ', main_weather)
    print('description: ', description)
    print('temperature: ', temperature - 272.15 ,"℃")           # convert temperature from kelvin to celsius degree

city_weather()
