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

def makeErrorMsgUsingArgs(msg_code, err_msg, *args) : 
    """[에러 메세지 양식에 맞게 만드는 함수]

    Args:
        msg_code ([string]): [메세지 코드]
        err_msg ([string]): [{숫자} 가 포함된 메세지 전체 내용] (constants.error.getErrorMsg())]
        args ([tuple]) : [{숫자} 위치에 삽입할 내용]

    Returns:
        [string]: [에러 메세지]
    """
    return concatStr(["[", msg_code, "] ", makeMessageUsingArgs(err_msg, args)])

def makeMessageUsingArgs(basic_str, *args) : 
    """[여러 인자를 이용해 메세지를 만드는 함수]

    Args:
        basic_str ([string]): [{숫자} 가 포함된 메세지 전체 내용]
        args ([tuple]) : [{숫자} 위치에 삽입할 내용]

    Returns:
        [string]: [양식에 맞게 만들어진 메세지]
    """
    idx = 0
    for arg in args : 
        basic_str = basic_str.replace(concatStr("{", idx, "}"), arg)
    return basic_str

def isCorrectType(variable, type) :
    """[변수가 원래 의도한 자료형이 맞는지 검사하는 함수]

    Args:
        variable ([object]): [확인할 변수]
        type ([object]): [확인 자료형]

    Returns:
        [bool]: [맞으면 true]
    """
    if type(variable) is not type : 
        return False
    else :
        return True