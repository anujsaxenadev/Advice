import requests
import os
from gtts import gTTS

# Getting responce from API from adviceslip.com
url = "https://api.adviceslip.com/advice"
language = 'en'
response = requests.get(url)

