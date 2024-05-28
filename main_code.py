from flask import Flask, render_template

app = Flask(__name__,
            static_url_path='',
            static_folder='.',
            template_folder='.'
            )

API_key = 913a3052e4518b0d4c14d67a6a54540e

def get_api(lat,lon):
    url = "https://api.openweathermap.org/data/2.5/weather?lat={" + lat + "}&lon={" + lon + "}&appid={" + API_key + "}"
    response = requests.get(url)
    
    if response.status_code == 200:
        print("GET successfull code 200")
        # note that the response content is webpage-like
        data_string = response.content.decode('utf-8')
        json_data = json.loads(data_string)
        return json.dumps(json_data, indent=2)

    else:
        print("erreur, ", response.status_code)


@app.route('/')
def index():
    return render_template("index.html")






# Lancement du serveur
# app.run(debug=True, use_reloader=False, host="0.0.0.0", port=80)