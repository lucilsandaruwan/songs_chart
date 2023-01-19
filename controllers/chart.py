# This file contains all the handler functions for menue options.
import views.validated_input as vi
import views.table as table
import views.graphs as graphs
import configs.language as lang
import models.chart_csv as chart_model
import configs.meta as meta
import views.str_decorators as sd
import views.process_controllers as ps




def top_ranked_songs_on_a_day():
    """This is handling the request of top ranked songs for a selected day. the functions is splitted as follows
            1. take date from user
            2. select shongs having rank less than or equal to 10 and display in a table
        Note: this is the handlar for menue option 1
    """
    # get validated date from user
    date = vi.validated_date(
        "%Y-%m-%d"
        , lang.str_by_lang_key("yyyy_mm_dd")
        , lang.str_by_lang_key("top_10_date")
    )

    # fetch top 10 songs for the selected date
    top_10 = chart_model.filtered_top_10_songs(date)
    # if songs are not available for the particular date, the function should stop execution
    if(len(top_10) == 0):
        print(lang.str_by_lang_key("no_songs_4_d_date").format(date))
        return

    song_len = meta.get_config("song_len")
    artist_len = meta.get_config("artist_len")
    #format the top 10 songs to draw table
    lable3 = "Rank"
    headers = (
        {"length": song_len + 4, "lable": "Song"}
        ,{"length": artist_len + 4, "lable": "Artist"}
        ,{"length": table.length_of_table_columns(lable3), "lable": lable3}
    )
    top_10_show = list(map(lambda x: (
        x["song"][0:song_len] + "..." if len(x["song"]) > song_len  else x["song"]
        ,x["artist"][0:artist_len] + "..." if len(x["artist"]) > artist_len  else x["artist"]
        ,x["rank"]
    ), top_10))

    # draw table
    table.dinamic_table(
        lang.str_by_lang_key("un_top_10_songs").format(date)
        ,headers
        ,top_10_show
    )

def artist_with_the_most_top_ranked_songs():
    """This is to print the artist who has most top ranked songs in the list.
       Top ranked can be defined in two ways
            1. artist having most number of songs having rank = 1
            2. artist having most number of songs withing top ranked songs (rank <= 10)
        The function is create by assiuming that the 1st definition is expected.
        *Note: this is the handler function for menue option 2
    """ 
    # get artists dictionry
    top_artists = chart_model.most_ranked_artist()
    
    # set headers with length to draw the songs table
    headers = (
        {"length": meta.get_config("song_len"), "lable": "Song"}
        ,{"length": table.length_of_table_columns("Top ranked times"), "lable": "Top ranked times"}
    )
    
    artist_names = list(top_artists.keys())
    if len(artist_names) == 1:
        # show most top ranked artists to user
        print(lang.str_by_lang_key("most_top_rnkd_artst").format(sd.warning(artist_names[0])))
    elif (len(artist_names) > 1):
        print(lang.str_by_lang_key("most_top_rnkd_artsts"), "\n")
        # iterate artists
        for i in range(len(artist_names)):
            print(sd.warning("\t{}. {}").format(i+1, artist_names[i]))
    if ps.exit_process("to see top ranked songs with the number or times became top"):
        return
    # iterate artists in top artists
    for artist_name, songs in top_artists.items():
        # create empty list
        songs_2_show = []
        labels = []
        values = []
        # iterate all the songs of selected artist
        for song, num_of_time_bng_1 in songs.items():
            # create touple of song name and the number of time being first, then add it into  songs_2_show list
            songs_2_show.append((
                song, num_of_time_bng_1
            ))
            # add song name and times being first to lables list
            labels.append(song + " ({})".format(num_of_time_bng_1))
            # add number of times being first to values list
            values.append(num_of_time_bng_1)

        table_title = lang.str_by_lang_key("s_wth_top_r_times").format(artist_name)
        # draw table
        table.dinamic_table(
            table_title
            ,headers
            ,songs_2_show
        )
        print(lang.str_by_lang_key("cls_popup"))
        # draw pie chart
        graphs.pie_chart(labels, values, table_title)
def longest_number_of_weeks():
    """ print songs having the 10 longest number of weeks on the board
        Note: this is the handler for menue option 3
    """    
    songs = chart_model.longest_week_on_board_10_songs()
    headers = (
        {"length": meta.get_config("song_len") + 4, "lable": "Song"}
        ,{"length": meta.get_config("artist_len") + 4, "lable": "Artist"}
        ,{"length": table.length_of_table_columns("Weeks on board"), "lable": "Weeks on board"}
    )
    # make empty lists to hold valuse to pass into views
    x = []
    y = []
    data_to_print = []
    # go through all the records and append array to be able to call the view to draw a table and bar chart.
    for key, s in songs.items():
        # trim the song title to 6 letters because name is too long to display in bar chart
        x.append(s["song"][0:6] + "...")
        y.append(int(s["weeks-on-board"]))

        data_to_print.append((
            s["song"][0:meta.get_config("song_len")] + "..." if len(s["song"]) > meta.get_config("song_len")  else s["song"]
            ,s["artist"][0:meta.get_config("artist_len")] + "..." if len(s["artist"]) > meta.get_config("artist_len")  else s["artist"]
            ,s["weeks-on-board"]
        ))
    
    # draw table
    table.dinamic_table(
        lang.str_by_lang_key("10_weeks_on_the_board")
        ,headers
        ,data_to_print
    )
    if ps.exit_process("to see songs in a bar chart"):
        return
    print(lang.str_by_lang_key("cls_popup"))
    # create bar chart for the songs of the artist
    c_meta = {
        "title": lang.str_by_lang_key("10_weeks_on_the_board")
        ,"xlable": lang.str_by_lang_key("sng_title")
        ,"ylable": lang.str_by_lang_key("wob")
        ,"x": x
        ,"y": y
        ,"color": "green"
    }
    graphs.bar_chart(c_meta)

def top_climber():
    """ Show top climbed song details and the details of other top 10 songs
        Note: this is the handler for menue option 4
    """
    songs = chart_model.top_10_climbers()
    # top climbed song
    if len(songs) > 0:
        # artist, song, rank, last-week, climb = songs[0]
        top_climbed = songs[list(songs.keys())[0]]
        print(lang.str_by_lang_key("top_climber"))
        print(lang.str_by_lang_key("top_climbed_song").format(
            sd.bold(top_climbed["song"])
            ,sd.bold(top_climbed["artist"])
            ,sd.bold(top_climbed["date"])
            ,sd.bold(top_climbed["rank"])
            ,sd.bold(top_climbed["last-week"])
            ,sd.bold(top_climbed["climb"])
        ))
    if ps.exit_process(lang.str_by_lang_key("to_see_other_climbers")):
        return
    # set headers of table with the column lengths 
    headers = (
        {"length": table.length_of_table_columns("yyyy-mm-dd"), "lable": "Date"}
        ,{"length": meta.get_config("artist_len") + 4, "lable": "Artist"}
        ,{"length": meta.get_config("song_len") + 4, "lable": "Song"}
        ,{"length": table.length_of_table_columns("Rank"), "lable": "Rank"}
        ,{"length": table.length_of_table_columns("Last week rank"), "lable": "Last week rank"}
        ,{"length": table.length_of_table_columns("Climb"), "lable": "Climb"}
    )
    # empty list
    data_to_print = []
    # go through all the records and append array to be able to call the view to draw a table.
    for key, x in songs.items():
        # crate touple with required elements for the table and append them to the data_to_print list
        data_to_print.append((
            x["date"]
            # trim the song title if it is too long to be shown in a table
            ,x["artist"][0:meta.get_config("artist_len")] + "..." if len(x["artist"]) > meta.get_config("artist_len")  else x["artist"]
            # trim the artist name  if it is too long to be shown in a table
            ,x["song"][0:meta.get_config("song_len")] + "..." if len(x["song"]) > meta.get_config("song_len")  else x["song"]
            ,x["rank"]
            ,x["last-week"]
            ,x["climb"]
        ))
    # draw table
    table.dinamic_table(
        lang.str_by_lang_key("10_climbers")
        ,headers
        ,data_to_print
    )

def top_songs():
    """ Shows the top 10 songs 
        the criteria to select top 10 songs is get the most 1st ranked song first.
        Note: this is the handler for 5
    """
    sorted_songs = chart_model.top_10_songs()
    
    headers = (
        {"length": meta.get_config("artist_len") + 4, "lable": "Artist"}
        ,{"length": meta.get_config("song_len") + 4, "lable": "Song"}
        ,{"length": table.length_of_table_columns("Number of times became first"), "lable": "Number of times became first"}
        ,{"length": table.length_of_table_columns("Climbed"), "lable": "Climbed"}
    )
    list_2_show = map(lambda song: (
        song["artist"][0:meta.get_config("song_len")] + "..." if len(song["artist"]) > meta.get_config("song_len")  else song["artist"]
        ,song["song"][0:meta.get_config("artist_len")] + "..." if len(song["song"]) > meta.get_config("artist_len")  else song["song"]
        ,song["number_of_top_times"]
        ,song["climb"]
    ), sorted_songs) 
    
    # draw table
    table.dinamic_table(
        lang.str_by_lang_key("top_songs")
        ,headers
        ,list_2_show
    )

def init():
    """ This is to call initialise functions of the application
    """
    chart_model.init_list()

