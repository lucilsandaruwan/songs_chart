import matplotlib.pyplot as plt

def bar_chart(meta):
    """ method to draw barchart according to the parameters from controller
        param p1: dictionary: having following values
                                title(string): The title to be shown
                                x(list): The list of values for x axis
                                y(list): The list of values for y axis
                                xlable(string): The lable of the x axis
                                ylable(string): The lable of the y axis
                                color(string): color of the bars
    """
    plt.style.use('ggplot')
    x = meta["x"]
    y = meta["y"]

    plt.bar(x, y, color= meta["color"])
    plt.xlabel(meta["xlable"])
    plt.ylabel(meta["ylable"])
    plt.title(meta["title"])
    # rotate axis labels
    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.show()

def pie_chart(lables, values, title):
    """ this view is to create pie chart
        param p1: list: should be a string list having lables of pie chart
        param p2: list: should be an integer list having values of each lable
        param p3: string: title of the pie chart
    """
    plt.pie(values, labels = lables)
    plt.title(title)
    plt.show() 