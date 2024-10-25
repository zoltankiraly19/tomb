from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Itt tároljuk a választható opciókat
DROPDOWN_OPTIONS = {
    "values": ["1", "2", "3"],
    "labels": ["Option 1", "Option 2", "Option 3"]
}

@app.route('/dropdown', methods=['GET', 'POST'])
def get_dropdown():
    """
    GET: Visszaadja a választható opciókat
    POST: Feldolgozza a kiválasztott opciót
    """
    if request.method == 'GET':
        return jsonify({
            "selectedOption": {
                "enum": DROPDOWN_OPTIONS["values"],
                "type": "string",
                "x-ui-widget": "dropdown",
                "x-enumLabels": DROPDOWN_OPTIONS["labels"],
                "title": "Válassz egy opciót"
            }
        })
    elif request.method == 'POST':
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