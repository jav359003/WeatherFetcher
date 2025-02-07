

import requests
import geocoder
import smtplib
import schedule
import time
from email.message import EmailMessage



API_KEY = "345a4720d2e677f200498affd54c6224"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
phone_number = '+18084699684'


def get_location():
    location = geocoder.ip('me')
    return location.latlng


def get_weather(API_KEY, lat, lon):
    request_url = f"{BASE_URL}?lat={lat}&lon={lon}&appid={API_KEY}&units=imperial"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        return f"The weather in your laptop's current location is {weather} and the temperature is {temperature}F."

    else:
        return 'An error occurred.'
def sendmail( to, subject, body):
    message = EmailMessage()
    message['subject'] = subject
    message['to'] = to
    message.set_content(body)

    user = 'javybaby494@gmail.com'
    message['from'] = user
    password = 'nkmmnjmnubwevosy'

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(message)

    server.quit()



def send_alerts():
    lat, lon = get_location()
    message= get_weather(API_KEY, lat, lon)
    sendmail('+18084699684@tmomail.net', 'Daily Weather Alert', message)


schedule.every().day.at("09:00").do(send_alerts)

while True:
    schedule.run_pending()
    time.sleep(1)