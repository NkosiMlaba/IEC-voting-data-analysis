import pandas as pd
import matplotlib.pyplot as plt
import json
import time

folder = None
file = None
party = None
year = None
selected_party_provinces = None

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
        file = data['cleaned_data_file'].replace("{}", str(year))
        selected_party_provinces = data['provinces']
        folder = data['folder'] + str(year)


def file_loader():
    """
    Construct the full file path using the global variables.

    Returns:
    str: The full file path.
    """

    path = folder + "/" + file
    return path


def plot_pie_chart(df):
    """
    Plot a pie chart of votes distribution by province for a specific party.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the voting data.
    """

    if party not in df['Party Name'].values:
        print(f'Party {party} not found in year {year}.')
        time.sleep(5)
        return

    selected_party = df[df['Party Name'] == party]

    if not selected_party.empty:
        votes_distribution = selected_party[selected_party_provinces].values.flatten()
        plt.figure(figsize=(10, 10))
        plt.pie(votes_distribution[:-1], labels=selected_party_provinces[:-1], autopct='%1.1f%%', startangle=140)
        plt.title(f'Votes Distribution by Province for {party}')
        plt.axis('equal')
        plt.show()


def main():
    """
    The main function to read configuration, load data, and plot the pie chart.
    """
    
    read_config("domain/config.json")
    df = pd.read_csv(file_loader())
    plot_pie_chart(df)

if __name__ == '__main__':
    main()