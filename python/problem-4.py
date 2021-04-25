# Project Euler - Problem 4
#  
# Largest palindrome product
# 
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def p4(digit):
    largest_palindrome = 1
    for num1 in range(10 ** digit):
        for num2 in range(10 ** digit):
            producted_num = str(num1 * num2)
            is_palindrome = False
            for index, num in enumerate(producted_num):
                if index >= len(producted_num) / 2:
                    break
                if num is producted_num[-1 - index]:
                    is_palindrome = True
                else:
                    is_palindrome = False
                    break
            if is_palindrome and int(producted_num) > largest_palindrome:
                largest_palindrome = int(producted_num)
    return largest_palindrome

if __name__ == "__main__":
    print(p4(2))  # This should be 9009
    print(p4(3))
