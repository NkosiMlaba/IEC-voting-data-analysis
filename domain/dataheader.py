import pandas as pd
import numpy as np
import config as current_data

folder = current_data.folder
file = current_data.formatted_data

def file_loader():
    path = folder + "/" + file
    return path

def drop_empty_columns(df):
    non_empty_columns = [col for col in df.columns if df[col].dropna().shape[0] > 0]
    return df[non_empty_columns]

def drop_rows_after_consecutive_empty(df, pattern):
    match_index = df.apply(lambda row: row.astype(str).str.contains(pattern).any(), axis=1).idxmax()
    df = df.iloc[:match_index]
    return df

if __name__ == '__main__':
    df = pd.read_csv(file_loader(), header=None)

    row_index_to_process = 1

    if row_index_to_process >= len(df):
        raise ValueError("Specified row index is out of range.")

    df = drop_empty_columns(df)

    for col in range(len(df.columns)):
        current_cell_value = df.iloc[row_index_to_process, col]

        if row_index_to_process > 0:
            cell_above_value = df.iloc[row_index_to_process - 1, col]
            
            if isinstance(cell_above_value, str) and cell_above_value.strip():
                df.iloc[row_index_to_process, col] = f"{cell_above_value} {current_cell_value}"
            else:
                if col > 0:
                    cell_left_value = df.iloc[row_index_to_process, col - 1]
                    
                    if isinstance(cell_left_value, str) and cell_left_value.strip():
                        df.iloc[row_index_to_process, col] = f"{cell_left_value} {current_cell_value}"

    df = df.drop(index=0).reset_index(drop=True)

    new_header = df.iloc[0]
    df.columns = new_header

    df.to_csv(folder  + '/cleaned_data.csv', index=False, header=False)
