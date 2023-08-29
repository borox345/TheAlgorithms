"""
Title: Multiples of 3 or 5
Description:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
Link: https://projecteuler.net/problem=1
"""

def checkNumber(num):
    if num % 3 == 0:
        return num
    elif num % 5 == 0:
        return num

if __name__ == "__main__":
    sum = 0
    for n in range(0, 1000):
        if checkNumber(n):
            x = checkNumber(n)
            sum += x
    
    print(sum)
