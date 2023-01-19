# this file is used to keep applicaton configs
import views.str_decorators as sd
import configs.language as lang

CONFIG = {
    "lang": "en"
    ,"csv_file_path": "data/charts.csv"
    ,"song_len": 46
    ,"artist_len": 46
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
        print(sd.error(lang.str_by_lang_key("meta_key_error").format(key)))
        