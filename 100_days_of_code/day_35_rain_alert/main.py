import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("API_KEY")
account_sid = os.environ.get("ACC_SID")
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": 33.921562,
    "lon": -78.020271,
    "appid": "a65a1aa5abe5fda0a737d24b794261de",
    "cnt": 4,  # from 6am to 6 pm
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
will_rain = False
for i in weather_data["list"]:
    condition_code = i["weather"][0]["id"]
    # list_of_weather_predictions.append(condition_code)
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, account_sid, http_client=proxy_client)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring the umbrella.",
            from_="+12057362627",
            to="Your verified number"
        )
print(message.sid)
