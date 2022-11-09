N = int(input())
List = list(map(int,input().split()))
# 가운데 인덱스를 찾고 0 1 2 3 4 5
###                0 1 2 5 5 6
start = 0
last = len(List)-1
ans = -1
while start <= last:
    mid = (start + last) // 2
    mid_val = List[mid]
    if mid < mid_val:
        last = mid - 1
    elif mid > mid_val:
        start  = mid + 1
    elif mid == mid_val:
        ans = mid
        break
print(ans)
