from flask import Flask, render_template
import pymysql
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<num>")
def up(num):
    if num == "favicon.ico":
        return "", 204
    '''
        1. numcount 테이블 생성(id, num, insert_at)
        2. pymysql로 연결
        3. 증가 한 수만큼 추가
        4. 연결끊기
        5. db 접속해서 조회
    '''
    print(num)
    dbdb = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='stydyuser2',
    password='q1w2e3',
    db='study'
    )
    cur=dbdb.cursor()
    cur.execute("insert into numcount(num) values(%s)", (num,))
    dbdb.commit()
    dbdb.close()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001)
