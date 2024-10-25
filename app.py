from flask import Flask, jsonify, request, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Az elérhető opciók a dropdown mezőhöz
options = [
    {"label": "Option 1", "value": "1"},
    {"label": "Option 2", "value": "2"},
    {"label": "Option 3", "value": "3"}
]

@app.route('/dropdown', methods=['GET'])
def get_dropdown():
    """
    Visszaadja a lenyíló mező opcióit JSON formátumban.
    """
    return jsonify({"options": options})

@app.route('/select_option', methods=['POST'])
def select_option():
    """
    Feldolgozza a felhasználó által kiválasztott opciót.
    """
    # Kiválasztott opció lekérése a kérésből
    selected_value = request.json.get("selectedOption")
    if not selected_value:
        abort(400, description="Missing 'selectedOption' in request body")

    # Ellenőrizzük, hogy az opció érvényes-e
    if selected_value not in [option["value"] for option in options]:
        abort(400, description="Invalid option selected")

    # Visszatérünk egy megerősítéssel
    return jsonify({
        "message": f"You selected: {selected_value}",
        "selectedOption": selected_value
    })

if __name__ == '__main__':
    app.run(debug=True)
