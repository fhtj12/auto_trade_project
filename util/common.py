from error.system import *

def formatNumber(num) :
    """[숫자 포맷]

    Args:
        num (integer): 정수

    Returns:
        string: 세자리수 단위로 콤마 처리된 문자열
    """
    return format(num, ',')

def concatStr(params) : 
    """[문자열 concat]

    Args:
        params ([list]): concat할 문자열들이 담긴 리스트

    Returns:
        [string]: 리스트의 문자열들을 모두 concat한 결과 문자열
    """
    if type(params) is not list : raise SystemError('ERR_PARAM_TYPE')
    return ''.join(map(str, params))

def makeErrorMsg(msg_code, err_msg) : 
    """[에러 메세지 양식에 맞게 만드는 함수]

    Args:
        msg_code ([string]): [메세지 코드]
        err_msg ([string]): [메세지 전체 내용 (constants.error.getErrorMsg())]

    Returns:
        [string]: [에러 메세지]
    """
    return concatStr(["[", msg_code, "] ", err_msg])