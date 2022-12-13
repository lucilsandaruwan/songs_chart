
def get_top_ranked_songs_on_a_day(chart, date, rank_limit):
    """ Filter songs for particular date and sort the filtered list from rank and song name
        :param p1: Dictionaries list holding songs details: chart
        :param p2: String date in "yyyy-mm-dd" format to filter songs
        :return: Dictionaries list having songs details
    """
    populated = list(filter(lambda c: c["date"] == date and int(c["rank"]) <= rank_limit, chart))
    populated.sort(key=lambda x: (int(x['rank']), x["song"]))
    return populated

def get_dates_having_songs(chart):
    """ Get all the disting dates in the chart order by the date
        :param p1: Dictionaries list having song details with date: chart
        :return: Set 
    """
    return sorted(set(map(lambda x: x["date"], chart)))

def get_portions_in_list(dates, limits, date_filter):
    """ This functions returns the available portions from the list of dates according to parameters
        :param p1: list this sould contains list of strings
        :param p2: dictionary this should have two elements offset and lenght to get the portion of string from the list
        :param p3: string the portion of string of the list to match 
    """
    if date_filter != "":
        dates = list(filter(lambda d: date_filter in d, dates))
    return sorted(set(map(lambda x: x[limits["offset"]:limits["length"]], dates)))