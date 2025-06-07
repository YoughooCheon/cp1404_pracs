"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task

is_finished = false
while not is_finished
    try
        result = integer value of user input "Enter a valid integer: "
        is_finished = true  # valid input, exit loop
    except ValueError
        print "Please enter a valid integer."

print "Valid result is:", result
"""
is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # Exit the loop when a valid integer is entered
    except ValueError:  # Catch ValueError if the input is not a valid integer
        print("Please enter a valid integer.")

print("Valid result is:", result)
