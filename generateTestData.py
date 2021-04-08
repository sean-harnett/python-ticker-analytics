import yfinance as yf
import pandas as pd

def generate_one_month_test_MSFT_data():
    msft = yf.Ticker("MSFT")
    return msft.history(str="1mo")


def write_test_to_csv(file_name, data_frame):
    data_frame.to_csv(file_name)

