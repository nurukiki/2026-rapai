from flask import Flask
#__name__은 누가 이 파일을 실행시키는지 파악할 수 있다.
#다른 파이썬 파일에서 이 모듈을 실행시켰을 땐 name은 hello가 됨
#이 모듈을 바로 실행하면 name은 main이 됨
app = Flask(__name__) 

@app.route('/')   #ip 주소 뒤에 붙는 주소
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
#host='0.0.0.0'은 누구나 접근 가능하도록 만듦
