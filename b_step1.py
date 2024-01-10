def my_euclidean(a, b):
    if (b==0):
        return a, 1, 0
    else:
        g, x1, y1 = my_euclidean(b, a%b)
        x = y1
        y = x1 - a//b*y1
        return g, x, y

a, b = map(int, input().split())
g, x, y = my_euclidean(a, b)
print(x, y)