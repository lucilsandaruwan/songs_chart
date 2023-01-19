# This file contains functions to rout user inputs withing the application. 
# It calls to handler functions of controllers according to user inputs.
from configs import language as lang
import views.validated_input as vi
import controllers.chart as chart_ctrl

def route():
    """ To display the menue and rout the selected menue number to relevent controller.
    """
    menue = lang.str_by_lang_key("menue_options")
    print(menue) 
    while True:
        #taking validated menue item number from user with the help of 'validated_input' view
        m_item = int(vi.defined_values(
            lang.str_by_lang_key("input_menue_option")
            ,(0,1,2,3,4,5,6,7)
            ,True
        ))
        if m_item == 0:
            print(menue)
        # Top ranked songs for a particular day
        elif m_item == 1:
            chart_ctrl.top_ranked_songs_on_a_day()
        elif m_item == 2:
            chart_ctrl.artist_with_the_most_top_ranked_songs()
        elif m_item == 3:
            chart_ctrl.longest_number_of_weeks()
        elif m_item == 4:
            chart_ctrl.top_climber()
        elif m_item == 5:
            chart_ctrl.top_songs()
        elif m_item == 6:
            print(lang.str_by_lang_key("msg_exit"))
            break
        elif m_item == 7:
            chart_ctrl.init()
def init():
    """This is the entry point of app. It calls login function from the controller to get shopper_id and rout function to rout
        user requests
    """
    chart_ctrl.init()
    route()   
# the entry point of the app which calls the init function to boot application
init()
