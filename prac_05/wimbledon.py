"""
CP1404/CP5632 Practical
wimbledon
URL: https://github.com/YoughooCheon/cp1404_pracs/blob/master/prac_05/wimbledon.py

function main
    set filename to "wimbledon.csv"
    set data to read_wimbledon_data(filename)

    set champions to count_champions(data)
    set countries_str, countries_count to extract_countries(data)

    display "Wimbledon Champions:"
    for each name, count in champions sorted by name
        display name and count

    display "These", countries_count, "countries have won Wimbledon:"
    display countries_str

function read_wimbledon_data(filename)
    open the file with encoding "utf-8-sig"
    skip the first line (header)
    for each remaining line
        split line by comma
        add resulting list to data list
    return data

function count_champions(data)
    create empty dictionary champions
    for each row in data
        get champion_name from column 2 (index 2)
        if champion_name in champions
            increment champions[champion_name] by 1
        else
            set champions[champion_name] = 1
    return champions

function extract_countries(data)
    create empty set country_set
    for each row in data
        add champion_country from column 1 (index 1) to country_set

    convert country_set to sorted list
    join list elements with ", " into countries_str
    return countries_str, length of country_set

main()
"""
import csv

def main():
    filename = "wimbledon.csv"
    data = read_wimbledon_data(filename)

    champions = count_champions(data)
    countries_str, countries_count = extract_countries(data)

    print("Wimbledon Champions:")
    for champ, wins in sorted(champions.items()):
        print(f"{champ} {wins}")

    print(f"\nThese {countries_count} countries have won Wimbledon:")
    print(countries_str)

def read_wimbledon_data(filename):
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        next(reader)
        return [row for row in reader]

def count_champions(data):
    champions = {}
    for entry in data:
        name = entry[2]  # Champion's name
        champions[name] = champions.get(name, 0) + 1
    return champions

def extract_countries(data):
    countries = {entry[1] for entry in data}  # Champion's country code
    sorted_countries = sorted(countries)
    countries_str = ", ".join(sorted_countries)
    return countries_str, len(countries)

if __name__ == "__main__":
    main()
