import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import currentdata as current_data
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

    plt.figure(figsize=(12, 8))
    plt.bar(selected_party_provinces, selected_party[selected_party_provinces].values.flatten())
    plt.xlabel('Provinces and Total Votes')
    plt.ylabel('Votes')
    plt.title(f'Votes by Province and Total Votes for {party}')
    plt.xticks(rotation=45, ha='right')
    plt.show()

if not selected_party.empty:
    votes_distribution = selected_party[selected_party_provinces].values.flatten()
    plt.figure(figsize=(10, 10))
    plt.pie(votes_distribution[:-1], labels=selected_party_provinces[:-1], autopct='%1.1f%%', startangle=140)
    plt.title(f'Votes Distribution by Province for {party}')
    plt.axis('equal')
    plt.show()