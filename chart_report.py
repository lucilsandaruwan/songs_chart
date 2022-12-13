import matplotlib.pyplot as plt
import numpy as np

def get_first_n_letters(string, number):
   """ This function is created to get the first n letters from a given string
       the function is used in plog_horizontal_bar_chart to trim y-axis lable if it is too long to display
   """
   return string if len(string) < number else string[0:number] + "..."


def plot_horizontal_bar_chart(x_data, y_data, x_lable, title):
    """ Drow horizontal bar charts according to paasing values
    :param p1: integers list to hold values for x-axis: x_data
    :param p1: strings list to hold values for y-axis: x_data
    :param p3: string lable for X axis: x_lable
    :param p4: string title of the graph: title
    :return: None
    """
    #trim and get the first 20 letters of lable for y-axix
    y_data = list(map(lambda x: get_first_n_letters(x, 50), y_data))

    plt.rcdefaults()
    plt.rcParams.update({'font.size': 7})

    fig, ax = plt.subplots()

    y_pos = np.arange(len(y_data))

    error = np.random.rand(len(y_data))

    ax.barh(y_pos, x_data, xerr=error, align="center")

    ax.set_yticks(y_pos, labels=y_data)

    ax.invert_yaxis()

    ax.set_xlabel(x_lable)

    ax.set_title(title, loc="left")
    fig.tight_layout()
    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()
    plt.show()


