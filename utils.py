

""" Given a list of strings, append them to create one string"""
def create_file_name_from_list(str_list, ticker_name):
    
    for element in str_list:  # Append the indicators as string list to the file_name
        ticker_name += ('_' + element.lower())
    return ticker_name