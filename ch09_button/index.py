from flask import Flask, render_template, jsonify
from model.button import Button as b1
from sensor.button import Button as b2

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/start", methods=["POST"])
def start():
    sensor = b2()
    data_dict = sensor.ms_reaction()

    if data_dict is None:
        return jsonify({"message": "시간 초과"}), 400

    db = b1()
    db.save(data_dict["ms"])

    return jsonify(data_dict)

@app.route("/api/stop", methods=["POST"])
def stop():
    return jsonify({"message" : "sorry.."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
