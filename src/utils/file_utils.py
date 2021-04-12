import os

import yaml

""" Given a list of strings, append them to create one string"""


def create_file_name_from_list(str_list, ticker_name):
    for element in str_list:  # Append the indicators as string list to the file_name
        ticker_name += ('_' + element.lower())
    return ticker_name


""" Function to construct a list of file names to parse from a directory. """


def parse_directory_file_names(directory_path: str):
    file_paths = list()
    file_names = list()
    for dirpath, dirnames, files in os.walk(directory_path):
        if len(dirnames) > 0:
            for dirname in dirnames:
                for file in files:
                    file_paths.append(dirpath + dirname + file)
                    file_names.append(file)
        else:
            for file in files:
                file_paths.append((dirpath + file))
                file_names.append(file)

    return file_paths, file_names


""" returns a list of dictionaries from a yaml file.
 Throws OSError when trying to open/read the file
  Or Throws a YAMLError when parsing with pyyaml"""


def parse_yaml(file_path: str):
    new_dict_list = list()
    try:
        with open(file_path, 'r') as file:
            try:
                yml = yaml.full_load(file)
                for obj, ob1 in yml.items():
                    new_dict_list.append({obj: ob1})
            except yaml.YAMLError:
                raise
    except OSError:
        raise

    return new_dict_list
