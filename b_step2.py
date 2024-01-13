def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


n, a, c = map(int, input().split())

is_ans_exist = False

for b in range(1, 1001):
    g = gcd(a, c)
    # print(g)
    g = gcd(g, b)
    # print(g)
    if n % g != 0:
        is_ans_exist = True
        print(b)
    # print("-----")
if not is_ans_exist:
    print(-1)