from random import randrange, getrandbits
import numpy as np
from math import gcd as bltin_gcd
import cryptomath
from datetime import datetime
import time


def is_prime(n, k=128):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True


def generate_prime_candidate(length):
    p = getrandbits(length)
    p |= (1 << length - 1) | 1
    return p


primes128 = []
primes256 = []
primes512 = []
primes1024 = []
primes1536 = []
primes2048 = []
primes3072 = []
primes4096 = []


def generate_prime_number(length):
    xx = 4
    while not is_prime(xx, 128):
        xx = generate_prime_candidate(length)
    return xx


file = open("128.txt", "r")
content = file.read().splitlines()
file.close()
for i in range(0, 46):
    primes128.append(int(content[i]))

file = open("256.txt", "r")
content = file.read().splitlines()
file.close()
for i in range(0, 46):
    primes256.append(int(content[i]))

file = open("512.txt", "r")
content = file.read().splitlines()
file.close()
for i in range(0, 46):
    primes512.append(int(content[i]))

file = open("1024.txt", "r")
content = file.read().splitlines()
file.close()
for i in range(0, 46):
    primes1024.append(int(content[i]))

file = open("1536.txt", "r")
content = file.read().splitlines()
file.close()
for i in range(0, 46):
    primes1536.append(int(content[i]))

file = open("2048.txt", "r")
content = file.read().splitlines()
file.close()
for i in range(0, 46):
    primes2048.append(int(content[i]))

file = open("3072.txt", "r")
content = file.read().splitlines()
file.close()
for i in range(0, 46):
    primes3072.append(int(content[randrange(0, 8000)]))

file = open("4096.txt", "r")
content = file.read().splitlines()
file.close()
for i in range(0, 46):
    primes4096.append(int(content[randrange(0, 8000)]))


# for i in range(0, 46):
#     numb = generate_prime_number(2048)
#     while bltin_gcd(numb, 65537) != 1:
#         numb = generate_prime_number(2048)
#     primes2048.append(numb)
#
# f = open("2048.txt", "w")
# for i in range(0, 46):
#     f.write(str(primes2048[i]))
#     f.write("\n")

def noCrt(x):
    return pow(x, d, n)


def CRT(x):
    m1 = pow(x, d, p)
    m2 = pow(x, d, q)
    h = qi * (m1 - m2) % p
    m = m2 + h * q
    return m


def currentMilliTime():
    return time.time_ns()


f = open("4096timeCRT.txt", "w")
for i in range(0, 45):
    for j in range(i + 1, 46):
        p = primes4096[i]
        q = primes4096[j]
        n = p * q
        e = 65537
        d = cryptomath.findModInverse(e, (p - 1) * (q - 1))
        dp = d % (p - 1)
        dq = d % (q - 1)
        qi = pow(q, -1, p)
        start = currentMilliTime()
        CRT(randrange(2, n-1))
        end = currentMilliTime()
        total = end - start
        f.write(str(total))
        f.write("\n")
f.close()
