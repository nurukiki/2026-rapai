import RPi.GPIO as GPIO
import time
import random

class Button:
    def __init__(self):
        self.LED_PIN = 8
        self.BUTTON_PIN = 36

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.LED_PIN, GPIO.OUT)
        GPIO.setup(self.BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def ms_reaction(self):
        GPIO.output(self.LED_PIN, GPIO.LOW)
        time.sleep(random.uniform(2.0, 4.0))

        GPIO.output(self.LED_PIN, GPIO.HIGH)
        start_time = time.perf_counter()

        while GPIO.input(self.BUTTON_PIN) == GPIO.HIGH:
            if time.perf_counter() - start_time >= 5:
                GPIO.output(self.LED_PIN, GPIO.LOW)
                return None
            time.sleep(0.001)

        end_time = time.perf_counter()
        GPIO.output(self.LED_PIN, GPIO.LOW)

        result_ms = (end_time - start_time) * 1000
        return {"ms": round(result_ms)}

    def closes(self):
        GPIO.cleanup()
