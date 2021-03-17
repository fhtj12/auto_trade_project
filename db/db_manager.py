from db.connection_pool import ConnectionPool as pool
from db.sql.sql_mapper import SqlMapper as sqlMapper

class DBManager : 
    def __init__(self) :
        """[생성자 - 커넥션을 pool에서 가져옴, 쿼리 실행용 커서 생성]
        """
        self.conn = pool.getConnection()
        self.cursor = self.conn.cursor()

    def __del__(self) : 
        """[소멸자 - pool 반환]
        """
        self.cursor.close()
        pool.releaseConnection(self.conn)

    def __enter__(self) : 
        """[생명주기 시작]
        """
        pass

    def __exit__(self, err_type, err_value, err_trace_back) : 
        """[생명주기 종료 - 커밋, 에러시 롤백 처리]
        """
        if err_type is not None : 
            self.conn.rollback()
        else :
            self.conn.commit()

    def select(self, query_id) : 
        """[select 쿼리]

        Args:
            query_id ([string]): [쿼리 식별 아이디 - (db.sql 경로의 쿼리를 정의해놓은 py 파일의 이름).(쿼리 함수명)]
            예시) test.fetchTest

        Returns:
            [object]: [쿼리 결과]
        """
        return self.cursor.execute(sqlMapper.getQuery('select', query_id))
