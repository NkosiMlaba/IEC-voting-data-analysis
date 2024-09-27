import pandas as pd
import matplotlib.pyplot as plt
import config as current_data

folder = current_data.folder
file = current_data.cleaned_data_file
party = current_data.party

def file_loader():
    path = folder + "/" + file
    return path

def plot_bar_chart(df):
    selected_party = df[df['Party Name'] == party]

    if not selected_party.empty:
        selected_party_provinces = [
            'Eastern Cape Votes',
            'Free State Votes',
            'Gauteng Votes',
            'KwaZulu-Natal Votes',
            'Limpopo Votes',
            'Mpumalanga Votes',
            'North West Votes',
            'Northern Cape Votes',
            'Western Cape Votes',
            'Out of Country Votes'
        ]
        selected_party_provinces.append('Total Votes')

        plt.figure(figsize=(12, 8))
        plt.bar(selected_party_provinces, selected_party[selected_party_provinces].values.flatten())
        plt.xlabel('Provinces and Total Votes')
        plt.ylabel('Votes')
        plt.title(f'Votes by Province and Total Votes for {party}')
        plt.xticks(rotation=45, ha='right')
        plt.show()

if __name__ == '__main__':
    df = pd.read_csv(file_loader())

    plot_bar_chart(df)