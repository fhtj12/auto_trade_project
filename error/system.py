from util import constants as const
from util import common

class SystemError(Exception) : 
    def __init__(self, msg_code) -> None:
        super().__init__(common.makeErrorMsg(msg_code, const.error.getErrorMsg(msg_code)))

    def __init__(self, msg_code, *args) -> None:
        super().__init__(common.makeErrorMsgUsingArgs(msg_code, const.error.getErrorMsg(msg_code), args))