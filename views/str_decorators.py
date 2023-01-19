# this file is created to format the prompt messages from a central point.
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def error(msg):
    return format(msg, FAIL)

def sucess(msg):
    return format(msg, OKGREEN)

def warning(msg):
    return format(msg, WARNING)

def underline(msg):
    return format(msg, UNDERLINE)

def bold(msg):
    return format(msg, BOLD)

def blue(msg):
    return format(msg, OKCYAN)

def format(msg, style):
    return style + str(msg) + ENDC