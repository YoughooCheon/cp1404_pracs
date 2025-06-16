"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia", "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"
}

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