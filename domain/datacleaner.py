import pandas as pd
import json

folder = None
file = None
party = None
year = None
selected_party_provinces = None

def is_empty_or_nan(x):
    """
    Checks if the input value `x` is either NaN or an empty string.
    
    Parameters:
    x (String): The input value to check.

    Returns:
    bool: True if the input value is either NaN or an empty string, False otherwise.
    """
    
    return pd.isna(x) or (isinstance(x, str) and x.strip() == '')


def convert_hash_to_string(x):
    """
    Checks if the input value `x` is a string starting with a '#' character 
    
    Parameters:
    x (any): The input value to check.

    Returns:
    The x as a string. Otherwise, returns the input value unchanged.
    """
    
    if isinstance(x, str) and x.startswith('#'):
        return str(x)
    return x


def file_loader():
    """
    Construct the full file path using the global variables.

    Returns:
    str: The full file path.
    """
    
    path = folder + "/" + file
    return path


def drop_rows_before(df, pattern):
    """
    Drop all rows before the first occurrence of a specified pattern.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    pattern (str): The pattern to search for in the DataFrame.

    Returns:
    pd.DataFrame: A DataFrame with rows before the first occurrence of the pattern removed.

    Raises:
    ValueError: If the pattern is not found in any row.
    """
    
    match_index = df.apply(lambda row: row.astype(str).str.contains(pattern).any(), axis=1).idxmax()
    df = df.iloc[match_index:]
    return df


def drop_rows_after_consecutive_empty(df):
    """
    Drop rows after encountering a specified number of consecutive empty rows.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    keep_rows (int): The number of rows to keep after the first empty row (default is 10).

    Returns:
    pd.DataFrame: A DataFrame with rows after the first empty row dropped, keeping the specified number of rows.
    """
    
    def is_empty(row):
        return row.isnull().all() or (row == '').all()
    
    for i, row in df.iterrows():
        if is_empty(row):
            return df.iloc[:i + 11]
    
    return df


def read_config(file_path):
    """
    Read configuration data from a JSON file and set global variables.

    Parameters:
    file_path (str): The path to the JSON configuration file.
    """
    
    global year, party, file, selected_party_provinces, folder
    with open(file_path, 'r') as file:
        data = json.load(file)

        year =  data['year'] 
        party = data['party']
        file = data["file"].replace("{}", str(year))
        selected_party_provinces = data['provinces']
        folder = data['folder'] + str(year)


def main():
    """
    The main function to read configuration, load data, and plot the pie chart.
    """
    
    read_config("domain/config.json")
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

if __name__ == '__main__':
    main()
