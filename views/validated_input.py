# this file contains functions to validate user input as per the requireent

import views.str_decorators as sd
import datetime
import configs.language as lang

def mandatory(message):
    """This is a recursive function to be used to get input which should not be empty 
       param p1: string: The message to show user to get input
        return: string/function:  return input if it is not empty or call the same function if the input is empty
    """
    value = input(message)
    if not value:
        return mandatory(message)
    else:
        return value

def defined_values(message, values, required):
    """This is a recursive function to be used to get input which should be in a defined list
        param p1: string: The message to show user to get input
        param p2: list: this should have the list of possible options for the input
        param p3: boolean: True if the fields should be none empty, False if the value can be empty
        return: string/function: return input if it is in the given list 
    """
    value = input(message)
    # convert elements in values to string
    values = list(map(str, values))
    # if user input should be nonempty and input is not set, need to give an error message to get an input value
    if required and not value:
        print(lang.str_by_lang_key("error_val_mandatory"))
        return defined_values(message, values, required)
    # if input has a nonempty value and it is not in the given list, need to give a warning that the entered value is not in option list
    elif value and value not in values:
        print(lang.str_by_lang_key("warning_sel_val_from").format(", ".join(values)))
        return defined_values(message, values, required)
    else:
        return value

def fix_length_number(message, length, required):
    """This is a recursive function to be used to get input which should be a number and contains defined numbers of digits.
        comonly used in credit card numbers
        param p1: string: The message to show user to get input
        param p2: string : The number of digits should be contains in the input
        param p3: boolean: True if the fields should be none empty, False if the value can be empty
        return: number/function: return input if it is a number having the defined number of digits
    """
    try:
        # convert input to a number, if it is not a numeric input it will trigger an exception
        value = int(input(message))
        # check the length of number
        if value and len(str(value)) != length:
            print(sd.error("\nThe number should have {} digits.".format(length)))
            return fix_length_number(message, length, required)
        else:
            return value
    except: # this is triggered if user enter some string wich can't be casted to int
        print(sd.error("\nPlease enter a number having {} digits.".format(length)))
        return fix_length_number(message, length, required)
        # raise 
    
def validated_date(format, u_r_format, message):
    """ This is to get date as a user input with validation
        param p1: string: The value shuld be according to the,
                        format of https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
                        example "%Y-%m-%d"
        param p2: string: this is the user readable format that should be displayed to user
                            ex "%Y-%m-%d" => "yyyy-mm-dd"
        param p3: string: The displaying message to collect value from user.
    """
    date_text = input(message)
    try:
        # convert message into date format, it will trigger an error if the input is not in date format
        date = datetime.datetime.strptime(date_text, format)
        # convert the date into yyyy-mm-dd format and return
        return datetime.datetime.strftime(date, format)
    except ValueError:
        # raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        print(lang.str_by_lang_key("warning_incorrect_data").format(u_r_format))
        return validated_date(format,u_r_format, message)