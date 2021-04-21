# Project Euler - Problem 1
# 
# Multiples of 3 and 5
# 
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def p1(max_number):

    multiple_numbers = list()

    for number in range(max_number):
        if number % 3 == 0 or number % 5 == 0:
            multiple_numbers.append(number)

    return sum(multiple_numbers)

if __name__ == "__main__":
    print(p1(10))   # To compare the result with number(23) in the question.
    print(p1(1000))
