from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORS engedélyezése minden domain számára

@app.route('/dropdown', methods=['GET'])
def get_dropdown():
    options = ["1", "2", "3"]
    return jsonify({"options": options})

if __name__ == '__main__':
    app.run(debug=True)
