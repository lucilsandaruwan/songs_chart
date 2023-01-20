# this file is used to keep applicaton configs

CONFIG = {
    "lang": "en"
    ,"csv_file_path": "data/charts.csv"
    ,"song_len": 46
    ,"artist_len": 46
    ,"str_styles": {
        "heaer": '\033[95m'
        ,"blue": '\033[94m'
        ,"green": '\033[92m'
        ,"warning": '\033[93m'
        ,"fail": '\033[91m'
        ,"bold": '\033[1m'
        ,"underline": '\033[4m'
    }
}

def get_config(key):
    """ this is to get meta config
    param p1: string: an index of the config dictionary to get value
    return: any(string, dictionary, list): the value of give key is returned, 
            if it is not exists, an error message and none will be returned
    """
    try:
        return CONFIG[key]
    except:
        print("'\033[91m'"+ "The config key '{}', is not available in /configs/meta.py.".format(key)
        ,"There can be errors in data where using this key\033[0m.\n" )
        