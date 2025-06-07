"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?

try
    numerator = integer value of user input "Enter the numerator: "
    denominator = integer value of user input "Enter the denominator: "

    if denominator = 0
        print "Cannot divide by zero!"
    else
        fraction = numerator divided by denominator
        print fraction

except ValueError
    print "Numerator and denominator must be valid numbers!"

print "Finished."
"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # Question 3: Avoid ZeroDivisionError by checking denominator before division
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    # Question 1: ValueError occurs when input cannot be converted to int
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
