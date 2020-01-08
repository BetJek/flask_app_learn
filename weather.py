import requests
import numpy as np 
import cv2

def weather():
    url = 'http://yandex.ru?'

    params = {
        'text': 'python'

    }
    result = requests.get(url,params=params)
    weather1 = result.json()
    return weather1

print(weather())