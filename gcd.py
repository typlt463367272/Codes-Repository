def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a = input()
b = input()
print (gcd(int(a), int(b)))
