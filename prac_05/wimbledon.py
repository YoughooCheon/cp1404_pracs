"""
CP1404/CP5632 Practical
wimbledon

function main
    set filename to "wimbledon.csv"
    set data to read_wimbledon_data(filename)

    set champions to count_champions(data)
    set countries_str, countries_count to extract_countries(data)

    display "wimbledon champions:"
    for each name, count in champions sorted by name
        display name and count

    display "these", countries_count, "countries have won wimbledon:"
    display countries_str

function read_wimbledon_data(filename)
    open the file with utf-8-sig encoding
    skip the first line (header)
    split each remaining line by comma
    return a list of lists (one row per list)

function count_champions(data)
    create an empty dictionary called champions
    for each row in data
        get champion_name from column 2
        if champion_name exists in champions
            increase their count by 1
        else
            add champion_name with count 1
    return champions

function extract_countries(data)
    create an empty set called country_set
    for each row in data
        add the champion_country from column 1 to country_set

    sort country_set into a list
    join the list into a string with ", "
    return the string and the number of countries

main()
"""
def main():
    """Main function to process and display Wimbledon champions."""
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
    """Read Wimbledon champions data from CSV and return a list of lists."""
    with open(filename, "r", encoding="utf-8-sig") as file:
        return [line.strip().split(",") for line in file.readlines()[1:]]

def count_champions(data):
    """Process data to count Wimbledon champions."""
    champions = {}
    for entry in data:
        name = entry[2]  # Champion's name (3rd column)
        champions[name] = champions.get(name, 0) + 1
    return champions

def extract_countries(data):
    """Extract unique countries of champions, sort, and return string and count."""
    countries = {entry[1] for entry in data}  # Champion's country (2nd column)
    sorted_countries = sorted(countries)
    countries_str = ", ".join(sorted_countries)
    return countries_str, len(countries)

if __name__ == "__main__":
    main()