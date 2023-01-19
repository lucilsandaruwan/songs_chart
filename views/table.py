# this view is created to display tables 
from views import str_decorators as sd

def dinamic_table(title, headers, data):
    """This is to drow tables according to the given headers and data. The number of element of hearers should be equal to the 
        number of elements in each record of data object to use this function. Refered https://www.educba.com/python-print-table/ 
        to build this function to match with the requirement of this application
        param p1: string: the title of the table
        praam p2: list: this should have list of dictionaries having following elements for each colomn of the table
                length: integer: The charactor length of the colomn
                lable: string: header lable to be printed
        param p3: list: this is a list of lists having values of each column in the header.
    """
    print("\n")
    print(sd.underline(sd.bold(title)))
    header_txt = "\n"
    # iterate headers and set headers
    for ele in headers:
        header_txt += "{1:<{0}}".format(ele["length"], ele["lable"])
    print(sd.bold(header_txt))
    
    # iterate data and draw table
    for item in data:
        data_txt = ""
        for k, v in enumerate(item):
            data_txt += "{1:<{0}}".format(headers[k]["length"], str(v))
        print(data_txt)

def length_of_table_columns(lable):
    """ This is to calculate the column length according to the header lable
        param p1: string: the header lable of the column
    """
    length = len(lable)
    return 5 if length <= 3 else length + 2