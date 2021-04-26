# Project Euler - Problem 6
#  
# Sum square difference
# 
# The sum of the squares of the first ten natural numbers is,
# ### see the https://projecteuler.net/problem=6 ###
# The square of the sum of the first ten natural numbers is,
# ### see the https://projecteuler.net/problem=6 ###
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
# 3025 − 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def p6(number):
    numbers = list(range(1, number + 1))
    sum_of_square = 0
    for number in numbers:
        sum_of_square += number ** 2
    square_of_sum = sum(numbers) ** 2
    difference = abs(sum_of_square - square_of_sum)
    return difference

if __name__ == "__main__":
    print(p6(10))  # 2640
    print(p6(100))
