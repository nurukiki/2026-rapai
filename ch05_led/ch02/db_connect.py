import pymysql

conn = pymysql.connect(host='localhost', user = 'sumin', password='q1w2e3', db = 'shopping_db')
cur = conn.cursor()
cur.execute("select * from customer");
row = cur.fetchall()
print(row)
cur.close()

conn.close()
