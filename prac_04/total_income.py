def main():
    """Display income report for incomes over a number of months."""
    number_of_months = int(input("How many months? "))  # 변수명 의미 있게 변경
    incomes = []

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))  # f-string 사용
        incomes.append(income)

    print("\nIncome Report\n-------------")
    display_income_report(incomes)


def display_income_report(incomes):
    """Display report showing income and cumulative total for each month."""
    total = 0
    for month_index, income in enumerate(incomes, start=1):  # enumerate 사용
        total += income
        print(f"Month {month_index:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()
