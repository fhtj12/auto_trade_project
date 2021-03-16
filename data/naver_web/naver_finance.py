from error.parameter import *
from util import constants as const
from util import web
from util import common
from error.parameter import *

def make_naver_finance_url(code, **kwargs) : 

    """[네이버 금융의 url을 생성해주는 함수]

    Args:
        code (string): 종목 코드

    Keyword Arguments:
        page (string): 찾을 페이지 번호

    Returns:
        [type]: [description]
    """

    if code is None : raise ParameterError()

    # 기본 url
    url = common.concatStr([const.url.getURL('URL_NAVER_ITEM'), code])

    # 가져올 page 추가
    page = kwargs.get('page', None)
    if page is not None :
        return web.appendJQuery(url, 'page', page)
