import pymysql

class Button:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='suminroot', password='q1w2e3', database='su1m1bx')

        self.cur = self.conn.cursor()
        self.cur.execute("""create table IF NOT EXISTS record_button(id int auto_increment primary key, ms int not null, created_at datetime not null default current_timestamp)""")
        print("connect ok!")
    
    def save(self, ms_value):
        try:
            self.cur.execute("INSERT INTO record_button (ms) VALUES (%s)", (ms_value,))
            self.conn.commit()
        finally:
            self.cur.close()
            self.conn.close()
