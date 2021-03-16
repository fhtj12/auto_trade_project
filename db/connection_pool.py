from pymysql import connect
from pymysqlpool.pool import Pool

pool = Pool(host="localhost", port=3306, user="root", password="1234", db="test")
pool.init()

connection = pool.get_conn()
cur = connection.cursor()
cur.execute('SELECT * FROM `pet` WHERE `name`=%s', args=("Puffball", ))
print(cur.fetchone())

pool.release(connection)