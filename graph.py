import pandas as pd
import mplfinance as mplf
import matplotlib.pyplot as plt
from utils import create_file_name_from_list
import numpy as np
## TODO: change ticker x axis, and y axis frequency
""" Method that reads a csv file into a data frame and sets the index to 'Date' column as datetime index """


def read_csv_into_data_frame(file_name):
    df = pd.read_csv(file_name)
    df = df.set_index(pd.to_datetime(df['Date']))
    return df


""" plot the dataframe's candlestick, and save it in a .png"""


def plot_base_graph_candlestick_to_png(data_frame, stock_name):
    mplf.plot(data_frame, type='candle', style='yahoo',
              savefig=(stock_name+'candlestick.png'))


""" Plot a candlestick, and various indicators all on one graph, and save it to a png file. """


def plot_indicator_graph_with_candlesticks(candlestick_data_frame, indicators_data_frame, stock_name, color_dictionary):

    # Get a list of the indicators that have been plotted
    indicators_used = indicators_data_frame.columns.tolist()


    file_name = create_file_name_from_list(indicators_used, stock_name) #  create a new file name based off of the stock_name

    ads = create_indicator_subplots(indicators_data_frame, color_dictionary)
  #  plt.xticks(np.arange(1,2, 1.0))
    #savefig=file_name+'.png'
    mplf.plot(candlestick_data_frame,style='yahoo', type='candle',addplot=ads) 
    mplf.show()

   


""" Add subplots to a list """
def create_indicator_subplots(indicators_data_frame, color_list):
    apd = []
    for column in indicators_data_frame:
        apd.append(mplf.make_addplot(indicators_data_frame[column], color=color_list[column] ) ) 
      
    return apd


""" function that reads and plots the csv candlestick to a png, returns the dataframe """



def read_and_plot_candlestick_to_png(file_name):
    df = read_csv_into_data_frame(file_name)
    plot_base_graph_candlestick_to_png(df, file_name)
    return df
