# Project Euler - Problem 5
#  
# Smallest multiple
# 
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def p5(min_number, max_number):
    numbers = list(range(min_number, max_number + 1))
    increasing_number = 2
    while True:
        is_multiple = True
        for number in numbers:
            if increasing_number % number != 0:
                is_multiple = False
                break
        if is_multiple:
            break
        increasing_number += 1
    return increasing_number

if __name__ == "__main__":
    print(p5(1, 10))  # 2520
    print(p5(1, 20))
