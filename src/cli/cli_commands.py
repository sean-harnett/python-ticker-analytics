import click

import src.graphing.ticker_graphs as t_g
import src.tick_analysis.indicator_calculations as ind_c
import src.utils.file_utils as f_uts


@click.command()
@click.option('--ticker_csv_file', prompt='Please enter csv file location for desired ticker',
              help='Path to the csv file containing ticker data', required=True)
@click.option('--indicators_yaml_file', prompt='Location of indicator yaml file',
              help='Path to yaml file containing indicators to plot', required=True)
@click.option('--ticker_name', prompt='What is the name of the ticker data?',
              help='The name of the investment stock - ie "MSFT"', required=True)
@click.option('--save_directory', prompt='Where do you want to save the output?', required=True,
              help='Path of the directory where you want to save the outputted graph.')
def cli(ticker_csv_file: str, indicators_yaml_file: str, ticker_name: str, save_directory: str):
    core_data_frame = t_g.read_csv_into_data_frame(ticker_csv_file)
    indicators: dict
    indicators = f_uts.create_indicators_from_yaml(indicators_yaml_file)
    indicator_data_frame, colors_dict = ind_c.calculate_indicators(indicators, core_data_frame)
    t_g.plot_indicator_graph_with_candlesticks(candlestick_data_frame=core_data_frame,
                                               indicators_data_frame=indicator_data_frame,
                                               stock_name=ticker_name, color_dictionary=colors_dict,
                                               saveorshow=True, save_location=save_directory)
