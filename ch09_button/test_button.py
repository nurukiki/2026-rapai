import RPi.GPIO as GPIO
import time

BUTTON = 36

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # 내부 풀업 저항 사용

print("버튼을 눌러보세요! (Ctrl + C 로 종료)")
try:
    while True:
        start = time.time()                                       # 기다리기 시작한 시각
        GPIO.wait_for_edge(BUTTON, GPIO.FALLING, bouncetime=50)   # 누를 때까지 기다림
        sec = time.time() - start                                 # 걸린 시간(초)
        print(f"누름! {sec:.2f}초 만에 누름")
except KeyboardInterrupt:
    GPIO.cleanup()
