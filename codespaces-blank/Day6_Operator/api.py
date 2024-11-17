"""
import requests
api_key='60e0bae47ae7038eaa8288b597d386f1'
city='kolkata'
url='https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=60e0bae47ae7038eaa8288b597d386f1&units=metric'

response=requests.get(url)
if response.status_code==200:
    weather_data=response.json()
    temp=weather_data['main']['temp']
    weather=weather_data['weather'][0]['description']
    humidity=weather_data['main']['humidity']
    with open("weather_report.txt","w") as file:
        file.write(f"weather report for {city}\n")
        file.write(f"temperature:{temp}\n")
        file.write(f"weather condition:{weather}\n")
        file.write(f"humidity:{humidity}%")
    print("weather report is successfully recorded")

"""
import requests
api_key='test_mJHJ3pf9ILOGrjdB7lXd5lM6RjHkVnpnqwonLfAc'
url= 'https://api.nettoolkit.com/v1/account/test-api-keys'

response=requests.get(url)
if response.status_code==200:
    codes=response.json()
    message=codes['code']
    with open("code_report.txt","w") as file:
        file.write(f"code {message}")
    print(f"code report is successfully loaded ")
else:
    print(f"website failed to load {response.status_code}")


