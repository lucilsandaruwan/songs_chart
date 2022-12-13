import csv
from meta_config import config_data as config
CHARTLIST = []
def get_file_handler():
    """ The function return a file handler to read data """
    fp = config["file_path"]
    try:
        fh = open(fp, mode='r')
        return fh
    except:
        print("Can't load the file, please check the whether the file is available in the path: " + fp)
        return None

def init_list():
    """ This is to load data data from csv file and store into the CHARTLIST global variable 
        if the csv data needs to be reload to the application, this function should be called
    """
    CHARTLIST.clear()
    print("Loading data from csv file. ")
    try:
        fh = get_file_handler()
        chart = csv.DictReader(fh)
        for i in chart:
            CHARTLIST.append(i)
        fh.close()
    except:
        print("File reader exception")

def get_as_a_list():
    """ This function should be used to get the data of csv file as a list
        Using this function, the chart list can be taken without reading csv file again and again
    """
    return CHARTLIST
