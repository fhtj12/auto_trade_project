class url : 
    """[웹 스크레이핑을 위한 url 상수 모음]

    Returns:
        [type]: [description]
    """

    __url_dict__ = {
        "URL_NAVER_ITEM" : "https://finance.naver.com/item/sise_day.nhn?code="
        , "URL_KRX_CORP_LIST" : "https://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13"
    }

    @staticmethod
    def getURL(url_code) : 
        return url.__url_dict__[url_code]

class error : 
    """[시스템 에러 메세지 모음]

    Returns:
        [type]: [description]
    """

    __msg__ = {
        "ERR_PARAM_REQUIRED" : "필수 파라미터가 없습니다."
        , "ERR_PARAM_TYPE" : "파라미터 타입이 틀립니다."
        , "ERR_SQL_TYPE" : "SQL 종류 설정이 잘못되었습니다."
    }

    @staticmethod
    def getErrorMsg(error_code) : 
        return error.__msg__[error_code]