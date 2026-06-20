from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["todo_db"]
collection = db["todos"]

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():

    data = request.get_json()

    item_name = data.get("itemName")
    item_description = data.get("itemDescription")

    todo = {
        "itemName": item_name,
        "itemDescription": item_description
    }

    collection.insert_one(todo)

    return jsonify({
        "message": "Todo item saved successfully"
    }), 201


if __name__ == "__main__":
    app.run(debug=True)