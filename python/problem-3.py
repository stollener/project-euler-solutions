# Project Euler - Problem 3
#  
# Largest prime factor
# 
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def p3(number):
    i = 2
    while number != 1:
        if number % i == 0:
            prime_factor = i
            number = number / i
        else:
            i += 1
    return prime_factor

if __name__ == "__main__":
    print(p3(13195))  # To check whether the largest prime factor is 29 for this number.
    print(p3(600851475143))
