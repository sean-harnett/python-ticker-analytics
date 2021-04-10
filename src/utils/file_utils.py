import yaml

""" Given a list of strings, append them to create one string"""


def create_file_name_from_list(str_list, ticker_name):
    for element in str_list:  # Append the indicators as string list to the file_name
        ticker_name += ('_' + element.lower())
    return ticker_name


""" returns a dictionary of indicators from a yaml file.
 Throws OSError when trying to open/read the file
  Or Throws a YAMLError when parsing with pyyaml"""


def create_indicators_from_yaml(file_name: str):
    items = {}
    try:
        with open(file_name, 'r') as file:
            try:
                indicators = yaml.full_load(file)
                #  add the indicators to a dictionary:
                for indicator, use in indicators.items():
                    items[indicator] = use
            except yaml.YAMLError as err:
                raise

    except OSError as exc:
        raise

    return items
