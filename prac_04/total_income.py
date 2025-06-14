"""
CP1404/CP5632 Practical
Starter code for cumulative total income program

function main
    ask user for number of months and store as num_months
    get_incomes with num_months and store the returned incomes list
    print_income_report with incomes list

function get_incomes(num_months)
    define incomes as an empty list
    for each month from 1 to num_months
        ask user to enter income for the month
        convert input to float and append to incomes
    return incomes

function print_income_report(incomes)
    print report header
    set total to 0
    for each index and income in incomes, starting index at 1
        add income to total
        print formatted line showing month number, income, and cumulative total

main
"""

def main():
    """Display income report for a given number of months."""
    num_months = int(input("How many months? "))
    incomes = get_incomes(num_months)
    print_income_report(incomes)


def get_incomes(num_months):
    """Get income values for the specified number of months."""
    incomes = []
    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    return incomes


def print_income_report(incomes):
    """Print income report with cumulative totals."""
    print("\nIncome Report\n-------------")
    total = 0
    for month_index, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {month_index:2} - Income: ${income:10.2f} Total: ${total:10.2f}")

main()

