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
    global year, party, file, selected_party_provinces, folder
    with open(file_path, 'r') as file:
        data = json.load(file)

        year =  data['year'] 
        party = data['party']
        file = data['cleaned_data_file'].replace("{}", str(year))
        selected_party_provinces = data['provinces']
        folder = data['folder'] + str(year)


def file_loader():
    path = folder + "/" + file
    return path


def plot_pie_chart(df):
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
    read_config("domain/config.json")
    df = pd.read_csv(file_loader())
    plot_pie_chart(df)

if __name__ == '__main__':
    main()