import pymysql

class DHT11:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='suminroot', password='q1w2e3', database='su1m1bx')

        #self.cur = self.conn.cursor(pymysql.cursors.DictCursor)        
        self.cur = self.conn.cursor()        
        self.cur.execute("""create table if not exists record_dht(id INT(11) NOT NULL AUTO_INCREMENT,humidity VARCHAR(5) NOT NULL, temperature VARCHAR(5) NOT NULL,created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(), PRIMARY KEY (id))""")
        print("connect ok!")

    def get(self):
        self.cur.execute("""select * from record_dht""")
        r = self.cur.fetchall()
        results = []
        for i in r:
            data = {
                    "id" : i[0],
                    "humidity" : i[1],
                    "temperature" : i[2],
                    "created_at" : i[3].strftime("%Y-%m-%d %H:%M:%S")
                }
            results.append(data)
        print(r)
        return results

    def save(self, temperature, humidity):
        self.cur.execute("INSERT INTO record_dht (temperature, humidity) VALUES (%s, %s)", (temperature, humidity))
        self.conn.commit()
        

