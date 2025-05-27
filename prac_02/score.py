"""
import random

define get_score_result(score)
    if score < 0 or score > 100
        return "Invalid score"
    if score >= 90
        return "Excellent"
    if score >= 50
        return "Passable"
    return "Bad"
end get_score_result

define main
    prompt user for score
    call get_score_result with user score and print result

    generate random score between 0 and 100
    call get_score_result with random score and print result
end main

run main
"""
import random

def get_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    score = float(input("Enter your score: "))
    result = get_score_result(score)
    print(f"Result for your score: {result}")

    random_score = random.randint(0, 100)
    random_result = get_score_result(random_score)
    print(f"Random score: {random_score}, Result: {random_result}")

main()
