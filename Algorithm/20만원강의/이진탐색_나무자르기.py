n,m = map(int,input().split())
List = sorted(list(map(int,input().split())))
st = 0
end = List[n-1]
Ans = 0
def cut(n, List):
    ans = 0
    for a in List:
        if a - n >= 0:
            ans += a - n
    return ans

while st < end:
    mid = (st + end) //2
    a= cut(mid, List)
    if a < m:
        end = mid -1
    elif a > m:
        st = mid + 1
    else:
        break



print(mid)

