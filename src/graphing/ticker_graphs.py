import matplotlib.ticker as ticker
import mplfinance as mplf
import pandas as pd

from src.utils.file_utils import create_file_name_from_list

#  TODO: change ticker x axis, and y axis frequency

""" Function that reads a csv file into a data frame and sets the index to 'Date' column as datetime index """


def read_csv_into_data_frame(file_name):
    try:
        df = pd.read_csv(file_name)
    except OSError as e:
        raise

    df = df.set_index(pd.to_datetime(df['Date']))
    return df


"""Read a list of files into seperate data frames."""


def read_bulk_files_to_data_frames(files: list):
    data_frames = list()
    for file in files:
        try:
            df = pd.read_csv(file)
            df = df.set_index(pd.to_datetime(df['Date']))
            data_frames.append(df)
        except OSError as e:
            raise
    return data_frames


""" Plot a candlestick, and various indicators all on one graph, and save it to a png file. """


def plot_indicator_graph_with_candlesticks(candlestick_data_frame: pd.DataFrame, indicators_data_frame: pd.DataFrame,
                                           stock_name: str, color_dictionary: dict, saveorshow: bool,
                                           save_location: str):
    # Get a list of the indicators that have been plotted
    indicators_used = indicators_data_frame.columns.tolist()

    file_name = save_location
    if file_name[-1] != '/' and file_name[-1] != '\\': # check for directory append
        file_name += '/'

    #  Create a new file name based off of the stock_name
    file_name += create_file_name_from_list(indicators_used, stock_name) + '.png'

    additional_plots = create_indicator_subplots(indicators_data_frame, color_dictionary)
    figure, axes = mplf.plot(candlestick_data_frame, style='yahoo', type='candle', addplot=additional_plots,
                             returnfig=True)
    axes[0].xaxis.set_major_locator(ticker.MultipleLocator(2))
    axes[0].set_title(' '.join(indicators_used))
    figure.suptitle(stock_name)
    # Either save the figure, or show it
    if saveorshow:
        print(file_name)
        figure.savefig(file_name)
    else:
        figure.show()


""" Add subplots to a list specific to mplFinance """


def create_indicator_subplots(indicators_data_frame, color_dict):
    additional_plot_list = []
    for column in indicators_data_frame:
        additional_plot_list.append(mplf.make_addplot(indicators_data_frame[column], color=color_dict[column]))

    return additional_plot_list
