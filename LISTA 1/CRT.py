import math

x = int(input("Enter x: "))
p = int(input("Enter p: "))
q = int(input("Enter q: "))
dp = int(input("Enter dp: "))
dq = int(input("Enter dq: "))
qi = int(input("Enter qi: "))


def encrypt(x):
    m1 = x**dp % p
    m2 = x**dq % q
    h = qi * (m1 - m2) % p
    m = m2 + h * q
    return m


print("Original value: ", x)
print("Encrypted: ", encrypt(x))
