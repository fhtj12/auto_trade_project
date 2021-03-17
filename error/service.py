from util import constants as const
from util import common

class ServiceError(Exception) : 
    def __init__(self, msg_code) -> None:
        super().__init__(common.makeErrorMsg(msg_code, const.error.getErrorMsg(msg_code)))