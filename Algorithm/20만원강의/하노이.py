n = int(input())
K = 0
ans = []
def hanoi(st, end, n):
    if n == 1:
        ans.append((st,end))
        return
    else:
        other = 6 - st -end
        hanoi(st, other, n-1)
        ans.append((st,end))
        hanoi(other, end , n-1)
hanoi(1,3,n)
print(len(ans))
for a in ans:
    c,d = a
    print(c,d)