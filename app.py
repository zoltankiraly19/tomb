from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/dropdown', methods=['GET'])
def get_dropdown():
    options = [
        {"label": "Option 1", "value": "1"},
        {"label": "Option 2", "value": "2"},
        {"label": "Option 3", "value": "3"}
    ]
    return jsonify({"options": options})

if __name__ == '__main__':
    app.run(debug=True)