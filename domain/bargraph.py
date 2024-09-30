import pandas as pd
import matplotlib.pyplot as plt
import sys
import json
import time


folder = None
file = None
party = None
year = None
selected_party_provinces = None

def read_config(file_path):
    global year, party, file, selected_party_provinces, folder
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

        year =  data['year'] 
        party = data['party']
        file = data['cleaned_data_file'].replace("{}", str(year))
        selected_party_provinces = data['provinces']
        folder = data['folder'] + str(year)

def file_loader():
    path = folder + "/" + file
    return path

def plot_bar_graph(df):

    formattted_csv = folder + "/cleaned_data.csv"
    df = pd.read_csv(formattted_csv)

    if party not in df['Party Name'].values:
        print(f'Party {party} not found in {year}.')
        time.sleep(5)
        return

    selected_party = df[df['Party Name'] == party]

    if not selected_party.empty:
        selected_party_provinces.append('Total Votes')

        plt.figure(figsize=(12, 4))
        plt.subplot(2, 1, 1)
        plt.bar(selected_party_provinces, selected_party[selected_party_provinces].values.flatten())
        plt.xlabel('Provinces and Total Votes')
        plt.ylabel('Votes')
        plt.title(f'Votes by Province and Total Votes for {party}')
        plt.xticks(rotation=45, ha='right')
        plt.show()

def main():
    read_config("domain/config.json")
    df = pd.read_csv(file_loader())
    plot_bar_graph(df)

if __name__ == '__main__':
    main()