import os
import json
import pandas as pd
import sys

import domain.bargraph as bargraph
import domain.piechart as piechart

config_path = "domain/config.json"
year = None
party = None

def print_election_years(files):
    clear_screen()
    output = "These are the available years for the election analysis:\n"
    for index, file in enumerate(files, start=1):
        output += f"{index}. {file}\n"
    print(output)


def print_parties(parties):
    global year
    clear_screen()
    output = f"These are the available parties for the {year} election year:\n"
    for index, file in enumerate(parties, start=1):
        output += f"{index}. {file}\n"
    print(output)


def fetch_election_years():
    """
    Show the available categories for the hangman game.

    Returns:
    str: The available categories for the hangman game.
    """
    files = []
    [files.append(f) for f in os.listdir('domain/data')]
    return files


def fetch_parties_in_election():
    global year
    file_path = f"domain/data/{year}/cleaned_data.csv"
    df = pd.read_csv(file_path)
    party_names = df.iloc[0:, 0].tolist()
    return party_names


def get_party_name():
    """
    Get the election year from the user.
    """
    parties = fetch_parties_in_election()
    print_parties(parties)
    
    categories = {str(index): file for index, file in enumerate(parties, start=1)}
    while True:
        number = input("Enter party number (e.g 1.): ")

        if number in categories.keys():
            category = categories[number]
            return category, f"\nYou chose the '{category.capitalize()}' for this analysis.\n"
            
        elif number.lower() == "exit" or number.lower() == "quit":
            return None, None

        else:
            text = "Invalid category number, try again\n"
            print(text)
            continue


def get_election_year():
    """
    Get the election year from the user.
    """
    files = fetch_election_years()
    print_election_years(files)
    
    categories = {str(index): file for index, file in enumerate(files, start=1)}

    while True:
        number = input("Enter category number (e.g 1.): ")

        if number in categories.keys():
            category = categories[number]
            return category, f"\nYou chose the '{category.capitalize()}' year for this analysis.\n"
            
        elif number.lower() == "exit" or number.lower() == "quit":
            return None, None

        else:
            text = "Invalid category number, try again\n"
            print(text)
            continue


def update_config_year(year_given):
    global config_path, year
    if config_path is None:
        raise ValueError("Configuration path is not set. Please run read_config() first.")
    
    with open(config_path, 'r') as file:
        data = json.load(file)

    data['year'] = year_given

    with open(config_path, 'w') as file:
        json.dump(data, file, indent=4)
    year = year_given


def update_party_in_config(party_given):
    global config_path, party
    if config_path is None:
        raise ValueError("Configuration path is not set. Please run read_config() first.")

    with open(config_path, 'r') as file:
        data = json.load(file)
    data['party'] = party_given
    with open(config_path, 'w') as file:
            json.dump(data, file, indent=4)
    party = party_given


def read_config(file_path):
    global year, party
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        year =  data['year']
        party = data['party']


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def process_pie_chart():
    clear_screen()
    print("Viewing pie chart analysis")
    piechart.main()


def process_bar_graph():
    clear_screen()
    print("Viewing bar graph analysis")
    bargraph.main()


def close_program():
    clear_screen()
    sys.exit("Exiting program...")


def main():
    read_config(config_path)
    
    while True:
        clear_screen()
        print(f"""Choose and option
    [1] Change year of election to analyse (current year is {year})
    [2] Change party to analyse (current party is {party})
    [3] View pie chart analysis
    [4] View bar graph analysis
    [5] Exit
            """)
        option_chosen = input("Enter option: ")
        if option_chosen == "1":
            category, text = get_election_year()
            if category:
                print(text)
                update_config_year(category)
                continue
            continue
        
        elif option_chosen == "2":
            category, text = get_party_name()
            if category:
                print(text)
                update_party_in_config(category)
                continue
            continue
        
        elif option_chosen == "3":
            process_pie_chart()
            continue
        
        elif option_chosen == "4":
            process_bar_graph()
            continue
        
        elif option_chosen == "5":
            close_program()
        
        else:
            print("Invalid option")
            continue

if __name__ == '__main__':
    main()