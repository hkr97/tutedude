from flask import Flask, request

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process():

    name = request.form.get("name")
    email = request.form.get("email")
    age = request.form.get("age")

    return {
        "name": name,
        "email": email,
        "age": age,
        "status": "success"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)