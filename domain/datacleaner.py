import pandas as pd
import config as config

folder = config.folder
file = config.file

def is_empty_or_nan(x):
    return pd.isna(x) or (isinstance(x, str) and x.strip() == '')

def convert_hash_to_string(x):
    if isinstance(x, str) and x.startswith('#'):
        return str(x)
    return x

def file_loader():
    path = folder + "/" + file
    return path

def move_outlier_value():
    for col in df.columns:
        non_empty_values = df[col].dropna()
        if len(non_empty_values) == 1:
            idx = non_empty_values.index[0]
            col_index = df.columns.get_loc(col)
            if col_index < len(df.columns) - 1: 
                next_col = df.columns[col_index + 1]
                df.at[idx, next_col] = df.at[idx, col]
                df.at[idx, col] = ''

def drop_rows_before(df, pattern):
    match_index = df.apply(lambda row: row.astype(str).str.contains(pattern).any(), axis=1).idxmax()
    df = df.iloc[match_index:]
    return df

def drop_rows_after_consecutive_empty(df):
    def is_empty(row):
        return row.isnull().all() or (row == '').all()
    
    for i, row in df.iterrows():
        if is_empty(row):
            return df.iloc[:i + 11]
    
    return df

if __name__ == '__main__':

    excel_file_path = file_loader()

    df = pd.read_excel(excel_file_path)
    
    first_header = "Free State"
    df = drop_rows_before(df, first_header)

    df.columns = df.iloc[0]

    df = df[1:]


    df.reset_index(drop=True, inplace=True)

    df = df.dropna(axis=1, how='all')

    if df.shape[1] >= 3:
        df.iloc[0, 2] = df.iloc[0, 1]
        df.iloc[0, 1] = ''

    df = df.map(convert_hash_to_string)

    df = df.loc[:, ~df.map(is_empty_or_nan).all()]
    
    # 
    df = drop_rows_after_consecutive_empty(df)
    if len(df) > 10:
        df = df[:-10]

    csv_file_path = folder + '/data.csv'

    df.to_csv(csv_file_path, index=False)

    print(f"Excel file '{excel_file_path}' has been successfully processed and saved to CSV file '{csv_file_path}'.")
