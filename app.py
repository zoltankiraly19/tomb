from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Itt tároljuk a választható opciókat
DROPDOWN_OPTIONS = {
    "values": ["1", "2", "3"],
    "labels": ["Option 1", "Option 2", "Option 3"]
}

@app.route('/dropdown', methods=['GET'])
def get_dropdown():
    """
    Visszaadja a választható opciókat a változóból
    """
    return jsonify({
        "type": "object",
        "properties": {
            "selectedOption": {
                "type": "string",
                "enum": DROPDOWN_OPTIONS["values"],
                "x-enumLabels": DROPDOWN_OPTIONS["labels"],
                "x-ui-widget": "dropdown",
                "title": "Válassz egy opciót"
            }
        },
        "required": ["selectedOption"]
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)