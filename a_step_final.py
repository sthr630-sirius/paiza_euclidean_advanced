def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

n = int(input())
books = [int(input()) for _ in range(n)]

g = books[0]
for i in range(1, n):
    g = gcd(g, books[i])
print(g)