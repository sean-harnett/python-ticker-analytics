import graph as g
from testData import generate_one_month_test_MSFT_data, write_test_to_csv
import indicators as ind
import matplotlib.pyplot as plt

import pandas as pd

## data_frame = generate_one_month_test_MSFT_data()

## write_test_to_csv('MSFT', data_frame)


core_data_frame = g.read_csv_into_data_frame('MSFT') ## get data_frame from file 'MSFT'

indicator_df = pd.DataFrame()

indicator_df['EMA'] = ind.calculate_EMA_from_data_frame(core_data_frame, 2)

indicator_df['ATR'] = ind.calculate_ATR_from_data_frame(core_data_frame, 2)

color_dictionary = {'EMA':'orange','ATR':'red'}

g.plot_indicator_graph_with_candlesticks(core_data_frame, indicator_df, 'MSFT', color_dictionary)






