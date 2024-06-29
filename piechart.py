import pandas as pd
import matplotlib.pyplot as plt
import currentdata as current_data
import sys

folder = current_data.folder
file = current_data.cleaned_data_file
party = current_data.party

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

def file_loader():
    path = folder + "/" + file
    return path

def plot_pie_chart(df):
    if party not in df['Party Name'].values:
        sys.exit(f'Party {party} not found in cleaned data.')

    selected_party = df[df['Party Name'] == party]

    if not selected_party.empty:
        votes_distribution = selected_party[selected_party_provinces].values.flatten()
        plt.figure(figsize=(10, 10))
        plt.pie(votes_distribution[:-1], labels=selected_party_provinces[:-1], autopct='%1.1f%%', startangle=140)
        plt.title(f'Votes Distribution by Province for {party}')
        plt.axis('equal')
        plt.show()


if __name__ == '__main__':
    df = pd.read_csv(file_loader())

    plot_pie_chart(df)