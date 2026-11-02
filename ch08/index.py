from flask import Flask, request, render_template, jsonify
from model.dht11 import DHT11
from datetime import datetime
from sensor.dht11 import get_now

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

@app.route('/api/now', methods=["POST"])
def now():
    values = get_now()

    if values is None:
        return jsonify({"error" : "센서 측정 실패"}), 503

    temp = values[0]
    hum = values[1]

    db = DHT11()

    try:
        db.save(temp, hum)
    finally:
        db.conn.close()

    result = {
            "temperature": temp,
            "humidity": hum,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
         }
    return jsonify(result)

@app.route('/api/record')
def record():
    db = DHT11()
    try:
        result = db.get()
    finally:
        db.conn.close()

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
