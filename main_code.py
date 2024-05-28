from flask import Flask, render_template

app = Flask(__name__,
            static_url_path='',
            static_folder='.',
            template_folder='.'
            )

api_key = '913a3052e4518b0d4c14d67a6a54540e'


import requests

def get_weather(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric',  # Utilisation des unités métriques (Celsius)
        'lang': 'en'  # Langue anglaise pour les descriptions
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather = [
            data['main']['temp'],       # temperature
            data['weather'][0]['description'],  # description
            data['main']['humidity'],   # humidity
            data['main']['pressure'],   # pressure
            data['wind']['speed']       # wind_speed
        ]
        return weather
    else:
        return None

city = "Paris"
w = get_weather(city)
print(w)



@app.route('/')
def index():
    return render_template("index.html")

@app.route("/get", methods=['GET'])
def ville():
    selected_city = request.args.get('city')
    data_json = get_weather(selected_city)

    return jsonify(data_json)





# Lancement du serveur
# app.run(debug=True, use_reloader=False, host="0.0.0.0", port=80)