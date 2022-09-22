import sys
# sys.stdin = open("input.txt")

N = int(input())
L = list(map(int,input().split()))
st = 0
la = N
while st < la:
    mid = (st + la) // 2
    if L[mid] > mid:
        st = mid
    elif L[mid] < mid:
        la = mid - 1
    elif L[mid] == mid:
        print(mid)
        break
