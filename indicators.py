import pandas_ta as ta


def calculate_EMA_from_data_frame(source_data_frame, period):
    return ta.ema(source_data_frame['Close'], length=period)


def calculate_ATR_from_data_frame(source_data_frame, period):
    return ta.atr(source_data_frame['High'], source_data_frame['Low'], source_data_frame['Close'], length=period)


def calculate_MA_from_data_frame(source_data_frame):
    return ta.ma(source=source_data_frame['Close'])


def calculate_MACD_from_data_frame(source_data_frame):
    return ta.macd(source_data_frame['Close'])

