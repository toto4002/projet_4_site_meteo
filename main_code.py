from flask import Flask, render_template

app = Flask(__name__,
            static_url_path='',
            static_folder='.',
            template_folder='.'
            )

@app.route('/')
def index():
    return render_template("index.html")


# Lancement du serveur
# app.run(debug=True, use_reloader=False, host="0.0.0.0", port=80)