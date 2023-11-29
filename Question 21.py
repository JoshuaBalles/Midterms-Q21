from flask import Flask, jsonify, request

app = Flask(__name__)

hearts = [
    {"heart_id": "0", "date": "25/11/2023", "heart_rate": "167bpm"},
    {"heart_id": "1", "date": "12/08/2023", "heart_rate": "197bpm"},
]


# 1. Create a new heart record and append it to the JSON file.
@app.route("/add_heart", methods=["POST"])
def add_heart():
    new_heart = request.get_json()
    hearts.append(new_heart)
    return jsonify({"message": "Heart record added successfully"}), 201


# 2. Read all heart information from the JSON file.
@app.route("/get_hearts", methods=["GET"])
def get_hearts():
    return jsonify({"hearts": hearts})


# 3. Read heart information of a specific heart_id from the JSON file.
@app.route("/get_heart/<string:heart_id>", methods=["GET"])
def get_heart(heart_id):
    heart = next((item for item in hearts if item["heart_id"] == heart_id), None)
    if heart:
        return jsonify({"heart": heart})
    else:
        return jsonify({"message": "Heart not found"}), 404


# 4. Update a heart record of a specific heart_id.
@app.route("/update_heart/<string:heart_id>", methods=["PUT"])
def update_heart(heart_id):
    heart = next((item for item in hearts if item["heart_id"] == heart_id), None)
    if heart:
        updated_heart = request.get_json()
        heart.update(updated_heart)
        return jsonify({"message": "Heart record updated successfully"})
    else:
        return jsonify({"message": "Heart not found"}), 404


# 5. Delete a heart record of a specific heart_id.
@app.route("/delete_heart/<string:heart_id>", methods=["DELETE"])
def delete_heart(heart_id):
    global hearts
    hearts = [item for item in hearts if item["heart_id"] != heart_id]
    return jsonify({"message": "Heart record deleted successfully"})


# Run the Flask app if this script is executed
if __name__ == "__main__":
    app.run()
