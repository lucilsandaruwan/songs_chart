import csv
from meta_config import config_data
import chart_model
import chart_processer as cp
import chart_report as cr

def get_date_portions(available_dates, d_p_name, date):
    """ The function returns the date portions available in dates lists 
        :param p1: list this should be a distinct dates list in yyyy-mm-dd format
        :param p2: string this should be one from (year/month/date)
        :param p3: string this should be the composed date from the available portion ex: 2022, 2022-01 or ""
        :return: string
    """
    input_message = config_data["date_input_msg"][d_p_name]
    date_portion_limits = config_data["date_portions"][d_p_name]
    ret = input(input_message)
    available_portions = cp.get_portions_in_list(available_dates, date_portion_limits, date)
    while(True):
        # list available options 
        if ret == "1":
            print(available_portions)
            ret = input(input_message)
        # wrong user input
        elif ret not in available_portions:
            print("There are no songs for the value you entered")
            ret = input(input_message)
        else:
            return ret

def top_ranked_songs_on_a_day():
    """ Plot top 10 songs in a horizontal bar chart, x-axis: rank, y-axis: song name and artist
        :param p1: None
        :return: None
    """
    date = ""
    chart = chart_model.get_as_a_list()
    available_dates = cp.get_dates_having_songs(chart)
    # get year from user to plot top songs
    date += get_date_portions(available_dates, "year", date)
    # get month from user
    date += "-" + get_date_portions(available_dates, "month", date)
    #get date from user
    date += "-" + get_date_portions(available_dates, "date", date)

    songs_to_plot = cp.get_top_ranked_songs_on_a_day(chart, date, 10)
    
    # set x and y axis data from the list
    y_data = [] 
    x_data = []
    for d in songs_to_plot:
        ele = "{} , \nby {}".format(d["song"], d["artist"])
        y_data.append(ele)
        x_data.append(int(d["rank"]))
    cr.plot_horizontal_bar_chart(x_data, y_data, "Rank", "Top 10 songs on {}".format(date))

def artistWithMostTopRankedSongs(): #TODO: need to implement
    print("Artist with most top ranked songs")
    chart1 = chart_model.get_as_a_list()
    print(chart1[11])

def songsWithLongestNumber(limit): #TODO: need to implement
    print("The 10 songs with the longest number of weeks on the board")
    chart = chart_model.get_as_a_list()
    print(chart[10])
    
def main():
    """ This is the entry point of the app and does few things
        1. prompt required messages and get user inputs to proceed
        2. Rout the user input to relevent function to generate reports
        :param p1: None
        :return: None
    """

    # initiate the chart model to load csv file into a list and store it as a global variable
    chart_model.init_list()

    # take the message to prompt user mentioning the possible input from config file to be used in different alerts.
    options = config_data["options"]

    # prompt start message
    print("Enter a number from the following list to proceed "
          + options
          )
    while True:
        try:
            # take user input
            reportType = int(input("\n\nEnter your option ( Enter 1 to list options):"))
            if reportType == 0:
                break
            elif reportType == 1:
                print(options)
            elif reportType == 2:
                chart_model.init_list()
            elif reportType == 3:
                top_ranked_songs_on_a_day()
            elif reportType == 4:
                artistWithMostTopRankedSongs()
            elif reportType == 5:
                songsWithLongestNumber(10)
            else: 
                # user input a different option which is not available in the options list
                print("\nYou have selected an invalid option. Please select one from the following list", options)
        except:
            # Handling exception like user enter nothing as option or any code issue
            print("\nSomething whent wrong, please try again with the following optoins", options)
            raise

main()