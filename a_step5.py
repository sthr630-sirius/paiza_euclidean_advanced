def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

n = int(input())
a = int(input())
g = a
for _ in range(n-1):
    b = int(input())
    g = gcd(g, b)
print(g)