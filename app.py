from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/dropdown', methods=['GET'])
def get_dropdown():
    options = ["1", "2", "3"]
    return jsonify({"options": options})

if __name__ == '__main__':
    app.run(debug=True)