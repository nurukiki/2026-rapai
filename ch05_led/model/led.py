import pymysql

class LED:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='sumin', password="q1w2e3", database="study")
        self.cur = self.conn.cursor()
        print("connect ok!! good")
    
    def get(self):
        query = "select * from record_led"
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def save(self, status):
        query = f"insert into record_led(status) values ('{status}')"
        self.cur.execute(query)
        self.conn.commit()
