import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 34.256290
MY_LNG = -118.573980
ENDPOINT_URL = "https://api.sunrise-sunset.org/json"

EMAIL = 'EMAIL'
PASSWORD = "Password"
EMAIL2 = 'EMAIL'

def is_iss_near():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()
    iss_lat = float(data['iss_position']['latitude'])
    iss_lng = float(data['iss_position']['longitude'])

    if iss_lng in range(int(MY_LNG-5), int(MY_LNG+5)) and iss_lat in range(int(MY_LAT-5), int(MY_LAT+5)):
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }
    response = requests.get(url=ENDPOINT_URL, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now <= sunrise or time_now >= sunset:
        return True
    else:
        return False

def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=EMAIL2,
                            msg="Subject: ISS IS OVERHEAD\n\n"
                                "The iss is over you. Take a look!"
                            )

while True:
    time.sleep(60)
    if is_night() and is_iss_near():
        send_email()
