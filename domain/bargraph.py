import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
import config as current_data
import sys

from io import StringIO

folder = current_data.folder
party = current_data.party

formattted_csv = folder + "/cleaned_data.csv"
df = pd.read_csv(formattted_csv)

if party not in df['Party Name'].values:
    sys.exit(f'Party {party} not found in cleaned data.')

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

    
    plt.figure(figsize=(12, 4))
    plt.subplot(2, 1, 1)
    plt.bar(selected_party_provinces, selected_party[selected_party_provinces].values.flatten())
    plt.xlabel('Provinces and Total Votes')
    plt.ylabel('Votes')
    plt.title(f'Votes by Province and Total Votes for {party}')
    plt.xticks(rotation=45, ha='right')
    plt.show()

def main():
    pass

if __name__ == '__main__':
    main()