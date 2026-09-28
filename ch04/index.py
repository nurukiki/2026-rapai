from flask import Flask, render_template
import pymysql


app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<num>")
def up(num):
    if num == "favicon.ico":
        return "",204

    '''
        1. numcount 테이블 생성(id, num, insert_at)
        2. pymysql로 연결
        3. 증가 한 수만큼 추가
        4. 연결끊기
        5. db 접속해서 조회
    '''
    print(num)
    db = pymysql.connect(
            host='localhost',
            port=3307,
            user='root',
            password='q1w2e3')
    cursor = db.cursor()
    
    cursor.execute("CREATE DATABASE IF NOT EXISTS test")
    cursor.execute("use test")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS numcount(
    id INT AUTO_INCREMENT PRIMARY KEY,
    num INT,
    insert_at DATETIME)
    """)


    cursor.execute("INSERT INTO numcount(num) VALUES(%s)", (num,))
    
    db.commit()
    db.close()
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
