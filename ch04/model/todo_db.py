import pymysql

class TodoDB:
    def __init__(self):
        self.conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='q1w2e3',
        database='study')
        self.cur=self.conn.cursor()
        print("connect ok")

    def get(self):
        sql="select * from todos"
        self.cur.excute(sql)
        values = self.cur.fetchall()
        return values

    def add(self,title):
        sql = f"insert into todos(task) values('{title}')"
        self.cur.excute(sql)
        self.conn.commit()

    def remove(self, todo_index):
        sql = f"delete from todos where todo_index = {todo_index}"
        self.cur.excute(sql)
        self.conn.commit()
