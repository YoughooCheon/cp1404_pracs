"""
cp1404/cp5632 - practical
sales bonus conversion program

display prompt for sales
get sales

while sales >= 0
    if sales is less than 1000
        calculate bonus = 10% of sales
    else
        calculate bonus = 15% of sales
    display bonus
    get sales

display "finished"
"""
sales = float(input("Enter sales: $"))

while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.10
    else:
        bonus = sales * 0.15
    print(f"Bonus: ${bonus:.2f}")
    sales = float(input("Enter sales: $"))

print("Finished")
