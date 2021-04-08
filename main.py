from src.graphing import ticker_graphs as g
from src.tick_analysis import indicator_calculations as ind

from src.utils import file_utils as ut

#  TODO: create command line interface, to run, and create application.

# data_frame = generate_one_month_test_MSFT_data()

# write_test_to_csv('MSFT', data_frame)

core_data_frame = g.read_csv_into_data_frame('MSFT') # get data_frame from file 'MSFT'


indicators_dict = ut.create_indicators_from_yaml('src/propertiesFiles/indicatorProperties.yaml')

indicator_df, color_dict = ind.calculate_indicators(indicator_dictionary=indicators_dict, source_data_frame=core_data_frame)

g.plot_indicator_graph_with_candlesticks(core_data_frame, indicator_df, 'MSFT', color_dict, saveorshow=False)






