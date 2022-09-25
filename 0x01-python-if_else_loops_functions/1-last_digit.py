#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
if n < 0:
    n = -1*n
n = n % 10

if n == 0:
    print("Last digit of ", number, "is", n, "and is zero")
elif n > 5:
    print("Last digit of", number, "is", n, "and is greater than 5")
elif n < 6 and n != 0:
    print("Last digit of", number, "is", n, "and is less than 6 and not 0")
