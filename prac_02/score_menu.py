"""
define get_valid_score
    prompt user for score
    while score is not between 0 and 100
        display error message
        prompt again
    return score
end get_valid_score

define get_score_result(score)
    if score < 0 or score > 100
        return "Invalid score"
    if score >= 90
        return "Excellent"
    if score >= 50
        return "Passable"
    return "Bad"
end get_score_result

define show_stars(score)
    print "*" repeated score times
end show_stars

define main
    score = get_valid_score
    display menu
    get user choice
    while choice is not "Q"
        if choice is "G"
            score = get_valid_score
        else if choice is "P"
            result = get_score_result(score)
            print result
        else if choice is "S"
            show_stars(score)
        else
            print invalid option message
        display menu
        get user choice
    print farewell message

run main
"""
def get_valid_score():
    """Prompt user for a valid score between 0 and 100."""
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Please enter between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score

def get_score_result(score):
    """Return result string based on score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):
    """Print as many stars as the score value."""
    print("*" * int(score))

def main():
    """Main function to run the score menu program."""
    score = get_valid_score()

    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")

    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(get_score_result(score))
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice")

        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input(">>> ").upper()

    print("Farewell!")

main()
