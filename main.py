from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def get_user():
    return jsonify({
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
