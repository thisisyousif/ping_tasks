import os
import requests
url = "https://render-telegram-bot-823k.onrender.com/"
response = requests.get(url)
print("Status Code:", response.status_code)
