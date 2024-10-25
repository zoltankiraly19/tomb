from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DROPDOWN_OPTIONS = {
    "values": ["1", "2", "3"],
    "labels": ["Első opció", "Második opció", "Harmadik opció"]
}

@app.route('/dropdown', methods=['POST'])
def submit_selected():
    selected = request.json.get('selectedOption')
    if selected in DROPDOWN_OPTIONS["values"]:
        return jsonify({
            "success": True,
            "message": f"Selected option: {selected}"
        }), 200
    return jsonify({
        "success": False,
        "message": "Invalid option"
    }), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)