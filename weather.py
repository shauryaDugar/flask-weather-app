from flask import Flask, render_template
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

list = ['Jaipur', 'New Delhi', 'allahabad']
my_api_key=os.environ.get('API_KEY')

@app.route('/')
def index():
    base_url = 'http://api.weatherapi.com/v1/current.json?key='+my_api_key
    weather_data=[]
    for city in list:
        url=base_url+'&q='+city
        r=requests.get(url)
        if r.status_code==400:
            continue
        print(r)
        weather_data.append(r.json())
    return render_template('weather.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)