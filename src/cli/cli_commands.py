import click

import src.graphing.ticker_graphs as t_g
import src.tick_analysis.indicator_calculations as indc
from src.graphing.ticker_graphs import read_bulk_files_to_data_frames
from src.utils.file_utils import parse_directory_file_names, parse_yaml

""" Main function to run the command line interface from (cli) """


@click.command()
@click.option('--yaml_properties', prompt='Please enter path to the yaml properties file',
              help='Path to .yaml file containing (1) csv source directory, (2) locators of a yaml file for indicators',
              required=True, default='src/propertiesFiles/source_data_properties.yaml')
@click.option('--save_directory', prompt='Where do you want to save the output?', required=True,
              help='Path of the directory where you want to save the outputted graph.')
def cli(save_directory: str, yaml_properties: str):

    props = parse_yaml(yaml_properties)
    csv_files, file_names = parse_directory_file_names(props[0]['file_properties']['csv_source_directory'])
    indicators = parse_yaml(props[0]['file_properties']['indicator_yaml_location'])

    source_data_frames = read_bulk_files_to_data_frames(csv_files)  # create a list of pandas.DataFrames
    ix = 0  # access file_names, the index corresponds to data_frames.

    for data_frame in source_data_frames:
        indicator_frame, colors = indc.calculate_indicators(indicator_dictionary=indicators[0],
                                                            source_data_frame=data_frame)
        t_g.plot_indicator_graph_with_candlesticks(candlestick_data_frame=data_frame,
                                                   indicators_data_frame=indicator_frame, stock_name=file_names[ix],
                                                   color_dictionary=colors, saveorshow=True,
                                                   save_location=save_directory)
        ix += 1


"""Handle errors that terminate the script."""


def handle_terminal_error(error_msg: str):
    click.secho(error_msg, fg='red')
    click.echo('Exciting script...')
    exit(1)
