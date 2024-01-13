def my_euclidean(a, b, c):
    if b == 0:
        #print(f"{a} * X + {b} * Y = {c}")
        #print(f"X = {c//a}, Y = {0}")
        return a, c//a, 0
    else:
        g, x1, y1 = my_euclidean(b, a%b, c)
        x = y1
        y = x1 - a//b*y1
        #print(f"{a} * X + {b} * Y = {c}")
        #print(f"X = {x}, Y = {y}")
        return g, x, y

n, p, a, b = map(int, input().split())
is_ans_exist = False

c = n-p
g, x0, y0 = my_euclidean(a, b, c)

min_i = - x0 // (b // g) - 1
max_i = (n - x0) // (b // g) + 1

for i in range(min_i, max_i):
    x = b//g * i + x0
    #print(f"x:{x}")
    # y = (c - a * x) // b
    if ((c - a * x) % b == 0):
        y = (c - a * x) // b
    else:
        break
    #print(f"y:{y}")
    if x >= 0 and y >= 0:
        #print(f"x:{x}")
        #print(f"y:{y}")
        is_ans_exist = True

c = n
g, x0, y0 = my_euclidean(a, b, c)

min_i = - x0 // (b // g) - 1
max_i = (n -x0) // (b // g) + 1

for i in range(min_i, max_i):
    x = b//g * i + x0
    #print(f"x:{x}")
    if ((c - a * x) % b == 0):
        y = (c - a * x) // b
    else:
        break
    #print(f"y:{y}")
    if x >= 0 and y >= 0:
        #print(f"x:{x}")
        #print(f"y:{y}")
        is_ans_exist = True

if is_ans_exist:
    print("Yes")
else:
    print("No")