# Project Euler - Problem 7
#  
# 10001st prime
# 
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def p7(number):
    count = 2
    prime_number = []
    while len(prime_number) < number:
        is_prime = True
        for i in range(2, count):
            if count % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_number.append(count)
        count += 1
    return prime_number[-1]

if __name__ == "__main__":
    print(p7(6))  # 13
    print(p7(10001))
