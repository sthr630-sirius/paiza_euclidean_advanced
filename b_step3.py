n, x, a, b = map(int, input().split())
is_ans_exist = False
for i in range(0, n//a+1):
    if ((n - a*i)%b == 0 and n - a*i >= 0) or ((n - x - a*i)%b == 0 and (n-x) - a*i >= 0):
        is_ans_exist = True
if is_ans_exist:
    print("Yes")
else:
    print("No")