import csv
from configs.meta import CONFIG as config
import configs.language as lang
CHARTLIST = []
def get_file_handler():
    """ The function return a file handler to read data """
    fp = config["csv_file_path"]
    try:
        fh = open(fp, mode='r')
        return fh
    except:
        print(lang.str_by_lang_key("err_csv_file_path").format(fp))
        return None

def init_list():
    """ This is to load data data from csv file and store into the CHARTLIST global variable 
        if the csv data needs to be reload to the application, this function should be called
    """
    CHARTLIST.clear()
    print(lang.str_by_lang_key("data_loading"))
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
def set_chart_list(clist):
    """This is to update list from other file. This is mainly used in unit testing
    param p1: list: a chart list to mock data
    """
    CHARTLIST.clear()
    for i in clist:
        CHARTLIST.append(i)

def filtered_top_10_songs(date):
    """ this is to select first 10 ranked songs for the given date and sort it according to rank
        param p1: string: a date in format yyyy-mm-dd
        return: list: list of dictionary having songs
    """
    populated = list(filter(lambda c: c["date"] == date and int(c["rank"]) <= 10, CHARTLIST))
    populated.sort(key=lambda x: (int(x['rank']), x["song"]))
    return populated

def artists_songs_with_times_of_ranked(rank):
    """ this to create dictionary to keep all artists as keys and thier top ranked songs s sub keys 
        And the number of times particular song become top ranked as the value.
        param: integer: expected rank
        return: dictionary: sample element, [artist][song] = "number of times that became fist ranked"
    """
    # create an empty dictionary 
    artists = {}
    # go throgh all the songs of chart
    for i in CHARTLIST:
        if int(i["rank"]) == rank:
            # set empty object if the artist is not available in the dictionary
            artists.setdefault(i["artist"], {})
            # set song for the created artist and set top rank number to 0 as default if the song is not available-
            # in the dictionary
            artists[i["artist"]].setdefault(i["song"], 0)
            # increment the top ranked time of the song of the artist 
            artists[i["artist"]][i["song"]] += 1

    return artists

def most_ranked_artist():
    """ This function returns a list of the most top ranked artists 
        return: list: the list contains the artists names who have most top ranked number of songs
    """
    artists = artists_songs_with_times_of_ranked(1)
    # create an integer and add value 0
    max_top_ranked_times = 0
    # create empty dictionary
    top_artists = {}

    # iterate artists 
    for artist, songs in artists.items():
        # create an integer with value 0
        top_ranked_times = 0
        # iterate songs
        for title, num_of_times_1 in songs.items():
            # add number of times being first of each song to top ranked times
            top_ranked_times += num_of_times_1
        # compare the max top ranked time with current artists top ranked time
        # if max top ranked times less than current artists top ranked times
        if max_top_ranked_times < int(top_ranked_times):
            # change max top ranked times as current artists top ranked times
            max_top_ranked_times = top_ranked_times
            # empty the dictionary as this artist has most ratings
            top_artists = {}
            # add songs to the new artist in the dictionary
            top_artists[artist] = songs
        # this to handle exception when multiple artists have same top ranked number
        # in this case, the top ranked times become equal
        elif max_top_ranked_times == int(top_ranked_times):
            # append the artists name to top artists list
            top_artists[artist] = songs
    return top_artists

def longest_week_on_board_10_songs():
    """get songs having the 10 longest number of weeks on the board
        return: dictionary: key => song + artist_name, value => weeks-on-board
    """
    # sort the chart by weeks-on-board in descending order
    sorted_chart = sorted(CHARTLIST, key=lambda x: int(x['weeks-on-board']), reverse=True)
    # make an empty dictionary
    no_dups = {}
    # make an empty set
    lng_nums = set()
    # go to the each record in sorted chart
    for song in sorted_chart:
        # exit loop if the number of element in lng_nums >= 10
        if(len(lng_nums) > 10):
            break
        else:
            # create unique key for songs
            sng_key = song["song"] + song["artist"]
            # set the songs details to no_dups from the first element of songs in the list
            no_dups.setdefault(sng_key, song)
            # add the week-on-board number to the set to get first 10 weeks-on-board numbers.
            lng_nums.add(no_dups[sng_key]["weeks-on-board"])
            #hack: remove the last element when the length become 11
            if len(lng_nums) > 10:
                del no_dups[sng_key]
    return no_dups

def songs_order_by_climb_number():
    """ this is to get songs order by the climb number (lastweek rank - rank)
        return: list: songs having climb number
    """
    # empty list
    climbed_songs = []
    # go through each song in the chart
    for song in CHARTLIST:
        # get last week rank is 0 or integer value
        rnk_lst_wk = 0 if song["last-week"] == "" else  int(song["last-week"])
        # get current rank
        rnk_currnt = int(song["rank"])
        # check the rank has been climed
        # add the climb element to song object
        song.update({"climb": rnk_lst_wk - rnk_currnt })
        # add the song with climb element to the climbed_songs list
        climbed_songs.append(song)

    # Sort the climbed songs list to get the 10 top climbed songs
    return sorted(climbed_songs, key=lambda x: x['climb'], reverse=True)

def top_10_climbers():
    """get songs that has most 10 highest climbed values. Calculate the difference
        between the last-week rank and current date rank and get the maximum climbed one from them
       return: dictionary: key => song + artists, value => song: dictionary
    """
    sorted_cl_songs = songs_order_by_climb_number()
    # empty dictionary to collect details of 10 songs
    de_dups = {}
    rnks = set()
    # go through each song in sorted songs
    for song in sorted_cl_songs:
        # check the length of de_dups list and break the loop
        if len(rnks) > 10:
            break
        # create unique key for songs
        ukey = song["song"] + song["artist"]
        # add the most high climed day of the song in to de_dups list
        de_dups.setdefault(ukey, song)
        rnks.add(de_dups[ukey]["climb"])
        # hack to remove additional value when break the loop in 11 song 
        if len(rnks) == 11:
            del de_dups[ukey]
    return de_dups

def top_10_songs():
    """this function to get the top songs. The definition of top songs as follows
            1. get the songs having number of times that song became first in ranking
            2. get the maximum climb of each song
            3. sort by the value of 1 in descending order and get songs having top 10 values
            4. iterate each song of the list returns in step 3 and get the highest climbed song from each top ranking numbered list
        return: list: list of songs having number of times became first and highest climb
    """
    ret = []
    l_number_climb = set()
    rank = 0
    while len(l_number_climb) <= 10 and rank <= 10:
        rank += 1
        artists = artists_songs_with_times_of_ranked(rank)
        songs_2_sort = []
        # iterate artists
        for artist, songs in artists.items():
            # iterate songs of artists
            for song, first_rnked_times in songs.items():
                
                # get songs and append them to the list to be sorted by first ranked times
                
                songs_2_sort.append((
                    {
                        "artist": artist,
                        "song": song,
                        "number_of_top_times": first_rnked_times
                    }
                ))
        sorted_songs_by_nott = sorted(songs_2_sort, key=lambda x: x['number_of_top_times'], reverse=True)
        length_list = set()
        # empty list
        d_to_sort_by_climb = {}
        climbed = songs_order_by_climb_number()
        for song in sorted_songs_by_nott:
            length_list.add(song["number_of_top_times"])
            first_climb = next((x for x in climbed if x["song"] == song["song"] and x["artist"] == song["artist"]))
            song["climb"] = first_climb["climb"]
            if len(length_list) > 10:
                break
            d_to_sort_by_climb.setdefault(song["number_of_top_times"], {})
            # print(d_to_sort_by_climb[song["number_of_top_times"]])
            d_to_sort_by_climb[song["number_of_top_times"]].setdefault(first_climb["climb"], [])
            d_to_sort_by_climb[song["number_of_top_times"]][first_climb["climb"]].append(song)
        while len(l_number_climb) <= 10 and len(d_to_sort_by_climb) > 0:    
            for top_time, climb_l in d_to_sort_by_climb.items():
                c_songs_keys = list(climb_l.keys())
                sorted_keys = sorted(c_songs_keys, key=lambda x: x, reverse=True)
                for key in sorted_keys:
                    if(len(l_number_climb) <= 10):
                        for song in climb_l[key]:
                            ret.append(song)
                    l_number_climb.add(str(top_time) + "_" + str(key))
                    del climb_l[key]
                
                # print(top_time, climb_l)
            d_to_sort_by_climb = {k: v for k, v in d_to_sort_by_climb.items() if len(v) > 0}
    return ret    
    
