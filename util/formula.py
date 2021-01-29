def getCAGR(fisrt, last, years) : 
    """[연평균 성장률 (CAGR) 구하기]

    Args:
        fisrt (integer): 최초 가격
        last (integer): 계산할 마지막 가격
        years (integer): 최초~마지막 사이의 연수

    Returns:
        float: 연평균 성장률 (소수 그대로)
    """
    return (last / fisrt) ** (1 / years) - 1

def getDailyPerChange(beforeData, nextData) : 
    """[일간 변동률]

    Args:
        beforeData (pandas.core.series.Series): 일별 종가 데이터
        nextData (pandas.core.series.Series): 일별 종가 데이터를 shift하여 며칠씩 뒤로 미룬 데이터 (1일을 미루면 1일 단위 변동률)

    Returns:
        pandas.core.series.Series: 일별 변동률
    """
    return (beforeData / nextData - 1) * 100

def getMaxDrawdown(min, max) : 
    """[최대 손실 낙폭 (MDD)]

    Args:
        min (integer): 최저점
        max (integer): 최고점

    Returns:
        float: 낙폭
    """
    return (min - max) / min