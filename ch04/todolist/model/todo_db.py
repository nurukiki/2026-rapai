import pymysql

class TodoDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost',port=3307, user='root', password='q1w2e3', db='test')
        self.cur = self.db.cursor()
        print("connect ok")

    def get(self):
        self.cur.execute("SELECT * FROM todos")
        return self.cur.fetchall()

    def add(self, task):
        sql = "INSERT INTO todos(task) VALUES(%s)"
        self.cur.execute(sql, (task,))
        self.db.commit()
    
    def delete(self, index):
        self.cur.execute(
            "DELETE FROM todos WHERE todo_index=%s",
            (index,)
        )
        self.db.commit()
