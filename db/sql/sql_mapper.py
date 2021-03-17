from db.sql.test import fetchTest
from error.system import *

class SqlMapper : 
    @staticmethod
    def createSqlMapper () : 
        pass

    @staticmethod
    def getQuery(sql_type, query_id) : 
        queryStr = query_router[query_id]()
        if queryStr.lower().startswith(sql_type) :
            return queryStr
        else : 
            raise SystemError('ERR_SQL_TYPE')

query_router = {
    "fetchTest" : fetchTest
}