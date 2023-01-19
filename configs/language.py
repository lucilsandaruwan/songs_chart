
## this file is used to keep all the prompt messages
## in case of multiple language support, this will help to do it
import configs.meta as m
import views.str_decorators as sd

# this dictinary object keeps the prompt messages for all languages.
# For this application en is used for english language.
LANG = {
    "en": {
        "menue_options": """\n\n{}
            \n 1 - Top ranked songs for a particular day
            \n 2 - Artist with the most top ranked songs 
            \n 3 - The songs with the 10 longest number of weeks on the board 
            \n 4 - Song that has moved the most in ranking on the board 
            \n 5 - The top songs
            \n 6 - Exit
            \n 7 - import the data from csv file if any change 
            \n 0 - Show menue
        """.format(sd.underline("MAIN MENU                                           "))
        ,"meta_key_error": sd.error("\nPlease add a correct {} in the file ./configs/meta.py to work this application.") 
        ,"lang_key_error": sd.warning("\nThere is an application error with language key {}. Please add a text to the key of LANG in ./configs.language.py")
        ,"input_menue_option": "\nPlease enter the number against the menue item or {} to see menue again: ".format(sd.blue("0"))
        ,"msg_exit": sd.sucess("Good bye! ")
        ,"warning_sel_val_from": sd.warning("\nPlease enter a value from {} ")
        ,"error_val_mandatory": sd.error("\nPlease enter a value, this is mandatory.")
        ,"warning_incorrect_data": sd.warning("Incorrect data format, should be {}")
        ,"top_10_date": "\nEnter the date in yyyy-mm-dd format to get top 10 songs: "
        ,"yyyy_mm_dd": " a valid date in yyyy-mm-dd format"
        ,"err_csv_file_path": sd.error("Can't load the csv file, please check whether the file is available in the path: {}")
        ,"un_top_10_songs": sd.underline("\nTop 10 songs of the day, {}                        ")
        ,"no_songs_4_d_date": sd.warning("\nThere are no songs for the entered date {}. Please try again with another date")
        ,"most_top_rnkd_artst": sd.sucess("\nThe artist with the most top ranked songs is: {} ")
        ,"most_top_rnkd_artsts": sd.sucess("\nThe artist with the most top ranked songs are")
        ,"s_wth_top_r_times":"Top ranked songs of {} with the number of times being top"
        ,"10_weeks_on_the_board": "The songs with the 10 longest number of weeks on the board"
        ,"10_climbers": sd.underline("The songs that has moved the most in ranking on the board")
        ,"top_songs": sd.underline("The top songs in the chart                                 ")
        ,"data_loading": sd.warning("Loading data from csv file.")
        ,"cls_popup": sd.warning("\nPlease close the popup window to continue .......")
        ,"sng_title": "Song Title"
        ,"wob": "Weeks on board"
        ,"top_climber": sd.sucess(sd.underline("\nThe song that has moved the most in ranking on the board"))
        ,"top_climbed_song":"""
            Song: {}
            Artist: {}
            Date: {}
            Rank: {}
            Last week rank: {}
            Climb (Last week rank - rank): {}
        """
        ,"input_10_climbed": "\nEnter {} or {}: ".format(
                                sd.blue("1 {}")
                                , sd.blue("0 to go back")
                            )
        ,"to_see_other_climbers": "to see other 10 most climbers details"
        ,
    }
}

def get_lang_conf():
    """ This is to get the language config according to the meta config file index
        If the index can't be found in LANG object, it returns an empty object with an error message.
        return: dictinary: The dictionary contains all the configs in the app for the lang key defined in ../meta.py file
    """
    try:
        lang = m.get_config("lang")
        return LANG[lang]
    except:
        print (LANG["en"]["meta_key_error"].format("language index (en)"))
        return {}

def str_by_lang_key(key):
    """ This is to take string from a language key.
        If the input string can't be found in LANG object, it will return an empty string with a warning.
        param p1: string: The key to get language string.
        return: string: The particular string for the key or empty string with a warning message-
                        if the given key is not exists in the LANG 
    """
    lang = get_lang_conf()
    try:
        return lang[key]
    except:
        print (lang["lang_key_error"].format(sd.blue(key)))
        return ""