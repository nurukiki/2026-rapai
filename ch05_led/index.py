from flask import Flask, request, render_template
import RPi.GPIO as GPIO
from model.led import LED


app = Flask(__name__)
led_model = LED()


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/on")
def led_on():
    try:
        GPIO.output(8, GPIO.HIGH)
        led_model.save("on")
        return "ok"
    except:   
        return "fail"

@app.route("/off")
def led_off():
    try:
        GPIO.output(8,  GPIO.LOW)
        led_model.save("off")
        return "ok"
    except:
        return "fail"

if __name__ == "__main__":
    led_model.get()
    app.run(host="0.0.0.0", port = 5002)


