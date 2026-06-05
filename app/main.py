from flask import Flask, request, jsonify

app = Flask(__name__)

SECRET_KEY = "admin123"  #an intentional vulnerability

@app.route("/")

def home():
    return jsonify({"message":"Open AI Secure CI/CD Pipeline running"})

@app.route("/login", methods=["POST"])
def login():
    data = request.json

    if data["password"] == SECRET_KEY:     #risky logic
        return jsonify({"status":"success"})

    return jsonify({"status":"failed"})

if __name__ == "__main__":
    app.run(debug=True)