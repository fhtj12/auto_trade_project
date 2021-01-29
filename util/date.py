from datetime import datetime, timedelta

def getYesterday(format = "%Y-%m-%d") : 
    """[어제 일자를 포맷에 맞게 가져옴.]

    Args:
        format (str, optional): 날짜 형식. Defaults to "%Y-%m-%d".

    Returns:
        string: [description]
    """
    return (datetime.now() - timedelta(days=1)).strftime(format)

def getToday(format = "%Y-%m-%d") :
    """[오늘 일자를 포맷에 맞게 가져옴.]

    Args:
        format (str, optional): 날짜 형식. Defaults to "%Y-%m-%d".

    Returns:
        string: [description]
    """
    return datetime.now().strftime(format)