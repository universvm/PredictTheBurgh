import pandas as pd


def load_data_df(dataset_dir, separator='            ', date_column='date'):
    loaded_df = pd.read_csv(dataset_dir, sep=separator)
    loaded_df.drop_duplicates(subset=date_column, inplace=True)
    loaded_df.dropna(inplace=True)
    return loaded_df

