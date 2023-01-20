# this file is created to format the prompt messages from a central point.
import configs.meta as m
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
    return format(msg, "fail")

def sucess(msg):
    return format(msg, "green")

def warning(msg):
    return format(msg, "warning")

def underline(msg):
    return format(msg, "underline")

def bold(msg):
    return format(msg, "bold")

def blue(msg):
    return format(msg, "blue")

def format(msg, style):
    stls = m.get_config("str_styles")
    if stls and style in stls.keys():
        msg = stls[style] + str(msg) + '\033[0m'
    return msg