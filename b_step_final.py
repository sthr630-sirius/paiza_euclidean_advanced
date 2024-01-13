def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

a, b, t = map(int, input().split())
g = gcd(a, b)
if t%g == 0:
    print("Yes")
else:
    print("No")