
STLS = 
def get_config(key):
    """ this is to get meta config
    param p1: string: an index of the config dictionary to get value
    return: any(string, dictionary, list): the value of give key is returned, 
            if it is not exists, an error message and none will be returned
    """
    try:
        return STLS[key]
    except:
        print(sd.error(lang.str_by_lang_key("meta_key_error").format(key)))