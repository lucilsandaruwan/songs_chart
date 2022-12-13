config_data = {
    "file_path": "data/charts.csv",
    "options": "\n 0 - Exit"
          "\n 1 - Show options"
          "\n 2 - Reload data from CSV file"
          "\n 3 - Top ranked songs for a particular day"
          "\n 4 - Artist with most top ranked songs "
          "\n 5 - The 10 songs with the longest number of weeks on the board "
          "\n 6 - song that has moved the most in ranking on the board "
          "\n 7 - The top songs ",
    "date_input_msg": {
        "year": "\nEnter the year in \"YYYY\" format to list songs or 1 to list available years: ",
        "month": "\nEnter the month in \"MM\" format to list songs or 1 to list available months: ",
        "date": "\nEnter the date in \"DD\" format to list songs or 1 to list available dates: "
    },
    "date_portions": {
        # yyyy-mm-dd
        "year": {"offset": 0, "length": 4},
        "month": {"offset": 5, "length": 7},
        "date": {"offset": 8, "length": 10}
    }
}
