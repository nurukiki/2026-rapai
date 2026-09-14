from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tntwk")
def 디비에 저장():
    데이터 입력
    주소 다시 불러오기:
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001)
