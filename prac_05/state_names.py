"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting

set code_to_name to {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia", "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}

set valid_state_codes to the set of keys from CODE_TO_NAME

function main
    print the entire code_to_name dictionary

    prompt user to "enter short state"
    convert input to uppercase and remove surrounding whitespace

    while input is not empty
        if input exists in code_to_name
            print "<input> is <full state name>"
        else
            print "invalid short state"
        prompt user again to "enter short state"
        convert input to uppercase and remove surrounding whitespace

if this file is run directly (not imported)
    main
"""
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia", "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}

VALID_STATE_CODES = set(CODE_TO_NAME.keys())

def main():
    """Prompt user for a short state code and display its corresponding name."""
    print(CODE_TO_NAME)

    state_code = input("Enter short state: ").strip().upper()
    while state_code:
        if state_code in CODE_TO_NAME:
            print(f"{state_code} is {CODE_TO_NAME[state_code]}")
        else:
            print("Invalid short state")
        state_code = input("Enter short state: ").strip().upper()


if __name__ == "__main__":
    main()