"""
CP1404/CP5632 Practical
State names and hex colours in dictionaries
File needs reformatting

"""
HEX_COLOURS = {"red3": "#cd0000", "black": "#000000", "brass": "#b5a642", "brilliantrose": "#ff55a3", "citron": "#9fa91f", "cornflowerblue": "#6495ed", "darkbyzantium": "#5d3954", "dutchwhite": "#efdfbb", "goldenrod": "#daa520", "indigo": "#4b0082"}

def main():
    print("Hex Color Lookup Program")
    get_hex_code()

def get_hex_code():
    while True:
        color_name = input("Enter a color name (or press Enter to quit): ").strip().lower().replace(" ", "")
        if not color_name:
            print("Exiting program.")
            break
        hex_code = HEX_COLOURS.get(color_name)
        if hex_code:
            print(f"The hex code for {color_name.title()} is {hex_code}.")
        else:
            print("Invalid color name. Please try again.")

if __name__ == "__main__":
    main()
