def gcd(a, b):
    if b == 1:
        return a
    else:
        return gcd(b, a % b)

a,b = input()
print (gcd(int(a), int(b)))
