import requests
import os
from gtts import gTTS

# Getting response from API from adviceslip.com
url = "https://api.adviceslip.com/advice"
language = 'en'
response = requests.get(url)

# Validating response and Playing advice.
if response:
	json = response.json()
	advice = json['slip']['advice']
	print("Advice")
	print(advice)
	voice = gTTS(text=advice, lang=language, slow=False) 
	voice.save("voice.mp3") 
	os.system("mplayer voice.mp3")
	os.remove("voice.mp3")
else:
    print('An error has occurred. Please check network your connection.')