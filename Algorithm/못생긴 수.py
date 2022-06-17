N = int(input())
d = [0] * N
def solve(a):
    if a%2 == 0:
        return a//2
    elif a%3 == 0:
        return a//3
    elif a%5 == 0:
        return a//5

    return False
for i in range(2, N):
    d[0] = 0
    d[1] = 1
    if solve(d[i])>0:
        solve(d[solve(d[i])])
    elif not solve(d[i]):
        continue