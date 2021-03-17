from pymysqlpool.pool import Pool

class ConnectionPool : 
    # private static variable
    __pool = Pool(host="localhost", port=3306, user="root", password="dlawls12", db="test")
    __pool.init()
    
    @classmethod
    def getConnection(cls) : 
        return cls.__pool.get_conn()

    @classmethod
    def releaseConnection(cls, connection) : 
        cls.__pool.release(connection)