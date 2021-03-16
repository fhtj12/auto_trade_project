from . import common

def appendJQuery(url, key, value) :
    return common.concatStr([url, "&", key, "=", value])