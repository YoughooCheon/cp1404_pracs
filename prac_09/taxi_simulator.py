"""
function main():
    print "Let's drive!"

    create list of taxis:
        - taxi named "Prius" with 100 fuel
        - silverservicetaxi named "Limo" with 100 fuel and fanciness 2
        - silverservicetaxi named "Hummer" with 200 fuel and fanciness 4

    set current_taxi to None
    set total_bill to 0

    define menu options: "q)uit, c)hoose taxi, d)rive"

    loop forever:
        print menu
        get user input choice (lowercase)

        if choice is 'q':
            break loop

        else if choice is 'c':
            print available taxis with indices
            try:
                get user input taxi_choice as integer
                if taxi_choice valid index:
                    set current_taxi to chosen taxi
                else:
                    print "Invalid taxi choice"
            except invalid input:
                print "Invalid taxi choice"

        else if choice is 'd':
            if current_taxi is None:
                print "You need to choose a taxi before you can drive"
            else:
                try:
                    get user input distance as float
                    if distance < 0:
                        print "Distance must be >= 0"
                        continue loop
                    current_taxi start new fare
                    drive current_taxi by distance
                    get trip cost from current_taxi
                    print trip cost formatted
                    add trip cost to total_bill
                except invalid input:
                    print "Invalid distance"

        else:
            print "Invalid option"

        print bill to date formatted

    print total trip cost formatted
    print "Taxis are now:"
    print each taxi with index

if running as main program:
    main()
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def main():
    """Run the interactive taxi simulator program."""
    print("Let's drive!")

    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    current_taxi = None
    total_bill = 0

    MENU = "q)uit, c)hoose taxi, d)rive"

    while True:
        print(MENU)
        choice = input(">>> ").lower()

        if choice == 'q':
            break

        elif choice == 'c':
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            try:
                taxi_choice = int(input("Choose taxi: "))
                if 0 <= taxi_choice < len(taxis):
                    current_taxi = taxis[taxi_choice]
                else:
                    print("Invalid taxi choice")
            except ValueError:
                print("Invalid taxi choice")

        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                try:
                    distance = float(input("Drive how far? "))
                    if distance < 0:
                        print("Distance must be >= 0")
                        continue
                    current_taxi.start_fare()
                    current_taxi.drive(distance)
                    trip_cost = current_taxi.get_fare()
                    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                    total_bill += trip_cost
                except ValueError:
                    print("Invalid distance")

        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

if __name__ == '__main__':
    main()
