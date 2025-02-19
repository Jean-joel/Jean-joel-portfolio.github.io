from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    # Traitement des données (ex : envoi de mail ou stockage en BDD)
    print(f'📩 Nouveau message de {name} ({email}): {message}')

    return jsonify({"status": "success", "message": "Message reçu !"})


if __name__ == '__main__':
    app.run(debug=True)
