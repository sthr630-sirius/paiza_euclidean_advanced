def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def lcm(a, b):
    return a*b // gcd(a, b)

n = int(input())
l = int(input())-1
for  _ in range(n-1):
    a = int(input())-1
    l = lcm(l,  a)

print(l)