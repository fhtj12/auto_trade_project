from pandas_datareader import data as pdr
from util import date
import yfinance as yf

yf.pdr_override()

def getData(code, **kwargs) :
    """[yahoo finance 주가 데이터]

    Args:
        code (string): 종목 코드

    Keyword Arguments:
        start_date (string): 조회를 시작할 일자(%Y-%m-%d) 없으면 어제까지
        end_date (string): 마지막 조회 일자(%Y-%m-%d) 없으면 금일자까지

    Returns:
        pandas.core.frame.DataFrame: 주가 데이터
    """
    start_date = kwargs.get('start_date', None)
    end_date = kwargs.get('end_date', None)
    if start_date == None :
        start_date = date.getYesterday()
    
    if start_date != None and end_date == None : # 위에서 정의됨.
        return pdr.get_data_yahoo(code, start = start_date)

    return pdr.get_data_yahoo(code, start = start_date, end = end_date)