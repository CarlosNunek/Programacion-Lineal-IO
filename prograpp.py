from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite todas las solicitudes CORS desde cualquier origen

@app.route('/api')
def api():
    return {'message': '¡Hola desde Flask!'}

if __name__ == '__main__':
    app.run(debug=True)
