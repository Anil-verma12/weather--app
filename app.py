from flask import Flask,render_template
import requests
from flask import request
import os

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def gfg():
    city = 'jaipur'
    if request.method == 'POST':
        city =request.form.get('city')
    else:
        response = requests.get('https://ipinfo.io/')
        data = response.json()
        city = data['city']
    def get_temp(city_name):
        '''required = city_name
        this function give as current temp of city
        min_temp and max_temp.'''
        api_key = '7c289fc082fcec061b596f629b7e4fe7'
        url = f"https://api.openweathermap.org/data/2.5/weather?"
        dict1 = {
            'q':city_name,
            'appid':api_key
        }
        resp = requests.get(url,params=dict1)
        resp
        if resp.status_code == 200:
            data = resp.json()
            current_temp = data['main']['temp']
            min_temp = data['main']['temp_min']
            max_temp = data['main']['temp_max']
            return current_temp,min_temp,max_temp
        else:
            msg = "on location"
            return msg
        
    cur_temp,min_temp,max_temp = get_temp(city)
    return render_template('Index.html',ct=cur_temp, mi = min_temp, mx = max_temp, ci = city)

    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Railway's assigned port
    app.run(host="0.0.0.0", port=port)
