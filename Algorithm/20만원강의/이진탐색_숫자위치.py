import sys
input = sys.stdin.readline
n = int(input())
List = list(map(int,input().split()))
List.append(9876543)
m = int(input())
st = 0
end = n
ans = 0
while end > st:
    mid = (st + end) // 2
    if List[mid] <  m:
        st  = mid + 1
    else:
        end = mid

print(st+ 1)