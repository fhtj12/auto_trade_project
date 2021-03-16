from util import constants as const

class ParameterError(Exception) : 
    def __init__(self) -> None:
        super().__init__(const.error.getErrorMsg('ERR_PARAM_REQUIRED'))

class ParameterTypeError(Exception) : 
    def __init__(self) -> None:
        super().__init__(const.error.getErrorMsg('ERR_PARAM_TYPE'))