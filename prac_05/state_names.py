"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia", "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"
}

VALID_STATE_CODES = set(CODE_TO_NAME.keys())

def get_state_name():
    """Prompt user for a short state code and display the corresponding state name."""
    print("Available State Codes:", ", ".join(VALID_STATE_CODES))

    state_code = input("Enter short state: ").strip().upper()
    while state_code:
        if state_code in VALID_STATE_CODES:
            print(f"{state_code} is {CODE_TO_NAME[state_code]}")
        else:
            print("Invalid short state. Please enter a valid code.")
        state_code = input("Enter short state: ").strip().upper()

if __name__ == "__main__":
    get_state_name()