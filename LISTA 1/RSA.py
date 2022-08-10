
x = int(input("Enter x: "))
n = int(input("Enter n: "))
e = int(input("Enter e: "))


def encrypt(x):
    en = x**e
    c = en % n
    return c


print("Original value: ", x)
print("Encrypted: ", encrypt(x))