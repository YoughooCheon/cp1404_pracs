"""
CP1404/CP5632 Practical
State names and hex colours in dictionaries
File needs reformatting

hex_colours = {"red3": "#cd0000", "black": "#000000", "brass": "#b5a642", "brilliantrose": "#ff55a3", "citron": "#9fa91f", "cornflowerblue": "#6495ed", "darkbyzantium": "#5d3954", "dutchwhite": "#efdfbb", "goldenrod": "#daa520", "indigo": "#4b0082"}

function main
    print "hex color lookup program"
    call get_hex_code
end function

function get_hex_code
    loop forever
        prompt user "enter a color name (or press enter to quit): "
        get input and convert to lowercase, remove spaces, save as color_name
        if color_name is empty then
            print "exiting program."
            break loop
        end if

        look up color_name in hex_colours dictionary
        if found then
            print "the hex code for [color_name title case] is [hex code]."
        else
            print "invalid color name. please try again."
        end if
    end loop
end function

if this file is main program then
    main
"""

HEX_COLOURS = {"red3": "#cd0000", "black": "#000000", "brass": "#b5a642", "brilliantrose": "#ff55a3", "citron": "#9fa91f", "cornflowerblue": "#6495ed", "darkbyzantium": "#5d3954", "dutchwhite": "#efdfbb", "goldenrod": "#daa520", "indigo": "#4b0082"}

def main():
    """Run the hex colour lookup program."""
    print("Hex Color Lookup Program")
    get_hex_code()

def get_hex_code():
    """Prompt for colour name and display hex code until blank input."""
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
