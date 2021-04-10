import pandas_ta as ta
from pandas import DataFrame


# Actual Indicator calls:

def calculate_EMA_from_data_frame(source_data_frame, period):
    return ta.ema(source_data_frame['Close'], length=period)


def calculate_ATR_from_data_frame(source_data_frame, period):
    return ta.atr(source_data_frame['High'], source_data_frame['Low'], source_data_frame['Close'], length=period)


def calculate_MA_from_data_frame(source_data_frame):
    return ta.ma(source=source_data_frame['Close'])


def calculate_MACD_from_data_frame(source_data_frame):
    return ta.macd(source_data_frame['Close'])


# Indicator helper Functions:

""" return a pandas.DataFrame() of a variable number of indicators
 based off of current dictionary boolean values, and a dictionary of colors for those indicators.
    :param source_data_frame is a pandas.DataFrame containing [Open, Close, High, Low] fields
    :param indicator_data_frame is a data_frame containing keys for each indicator, whose values are another dictionary.
"""


def calculate_indicators(indicator_dictionary, source_data_frame):
    calculated_indicators = DataFrame()
    color_dict = {}
    if indicator_dictionary['indicators']['EMA']['use']:
        calculated_indicators['EMA'] = calculate_EMA_from_data_frame(source_data_frame,
                                                                     indicator_dictionary['indicators']['EMA'][
                                                                         'period'])
        color_dict['EMA'] = indicator_dictionary['indicators']['EMA']['color']
    if indicator_dictionary['indicators']['ATR']['use']:
        calculated_indicators['ATR'] = calculate_EMA_from_data_frame(source_data_frame,
                                                                     indicator_dictionary['indicators']['ATR'][
                                                                         'period'])
        color_dict['ATR'] = indicator_dictionary['indicators']['ATR']['color']
    if indicator_dictionary['indicators']['MA']['use']:
        calculated_indicators['MA'] = calculate_EMA_from_data_frame(source_data_frame,
                                                                    indicator_dictionary['indicators']['MA']['period'])
        color_dict['MA'] = indicator_dictionary['indicators']['MA']['color']
    if indicator_dictionary['indicators']['MACD']['use']:
        calculated_indicators['MACD'] = calculate_EMA_from_data_frame(source_data_frame,
                                                                      indicator_dictionary['indicators']['MACD'][
                                                                          'period'])
        color_dict['MACD'] = indicator_dictionary['indicators']['MACD']['color']

    return calculated_indicators, color_dict
