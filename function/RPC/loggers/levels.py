
DEBUG = 3
INFO = 2
CRITICAL = 1
REPORTER = 0

def get_name(level):
    if level == 0:
        return 'REPORTER'
    elif level == 1:
        return 'CRITICAL'
    elif level == 2:
        return 'INFO'
    elif level == 3:
        return 'DEBUG'
    else:
        return 'UNKNOWN level type: ' + str(level)