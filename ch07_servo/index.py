from flask import Flask, request, render_template, jsonify
import RPi.GPIO as GPIO
from time import sleep

app = Flask(__name__)

pin = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
servo = GPIO.PWM(pin, 50) # pin을 PWM 모드 50Hz로 사용

#서보모터는 펄스 폭(듀티비)에 따라 각도가 정해지기 때문에
#사용자 편의를 위해 각도(angle)를 듀티사이클(duty)로 변환해 사용한다.
def setAngle(angle):
    duty =round( 2.5 + (10 * angle / 180), 1)
    print(f"degree : {angle} to {duty}(duty)")
    servo.ChangeDutyCycle(duty)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/angle', methods=['POST'])
def control_servo():
    data = request.get_json()
    angle = data.get('angle')  # POST 요청에서 'angle' 값을 가져옴
    if angle is not None:
        setAngle(int(angle))  # 서보 모터 각도 설정
        return jsonify({'message': 'angle set to {}'.format(angle)})
    else:
        return jsonify({'message': 'fail! check your parameter'})


if __name__ == '__main__':
    try:
        servo.start(0)
        app.run(host='0.0.0.0', port=5002, debug=False)
    except KeyboardInterrupt:
        pass
    finally:
        servo.stop()
        GPIO.cleanup()

