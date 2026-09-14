import pymysql

conn = pymysql.connect(host="localhost", user='root', password="q1w2e3", db="shopping_db")
cur = conn.cursor()
cur.execute("select * from CUSTOMER")
results = cur.fetchall()
print(results)

cur.close()
conn.close()
