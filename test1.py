from flask import Flask, jsonify, request
from data1 import data1

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data": data1,
        "message": "success"
    }), 200

@app.route("/star")
def planet():
    name = request.args.get("name")
    planet_data = next(item for item in data1 if item["name"] == name)
    return jsonify({
        "data": planet_data,
        "message": "success"
    }), 200

if __name__ == "__main__":
    app.run()
