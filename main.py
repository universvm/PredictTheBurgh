from config import DATA_PATH, DATE_COLUMN, SEP

from processing.data_processing import load_data_df

if __name__ == '__main__':
    stock_data = load_data_df(DATA_PATH, separator=SEP,
                              date_column=DATE_COLUMN)

    # print(stock_data[stock_data.columns[7]])
    print(stock_data.info())
    stock_data.dropna(inplace=True)
    # print(stock_data[stock_data.columns[7]])
    print(stock_data.info())

