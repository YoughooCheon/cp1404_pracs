"""
CP1404/CP5632 - Practical
loops conversion program

get n

a. count in 10s from 0 to 100
for i from 0 to 100 step 10
    print i with space

print newline

b. count down from 20 to 1
for i from 20 down to 1 step -1
    print i with space

print newline

c. print n stars on one line
for i from 1 to n
    print '*'

print newline

d. print n lines of increasing stars
for i from 1 to n
    print '*' repeated i times
"""
n = int(input("Number of stars: "))

# a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c
for i in range(n):
    print('*', end='')
print()

# d
for i in range(1, n+1):
    print('*' * i)
