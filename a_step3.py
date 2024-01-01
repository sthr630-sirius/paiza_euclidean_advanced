def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def lcm(a, b):
    return a*b//gcd(a, b)

n = int(input())
a = int(input())
b = int(input())
g = gcd(a, b)
l = lcm(a, b)
for _ in range(n-2):
    b = int(input())
    g = gcd(g, b)
    l = lcm(l, b)
print(g)
print(l)