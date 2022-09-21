# 이진탐색은 기본적으로 정렬된 상태여야 구할 수 있음
import sys
sys.stdin = open("input.txt")
for _ in range(4):
    ans = -1
    # print(sys.stdin.readline())
    N,x = map(int,sys.stdin.readline().split())
    L = list(map(int,sys.stdin.readline().split()))
    st = 0
    la = N
    st2 = 0
    la2 = N
    while st < la:
        mid = (st + la)// 2
        if L[mid] >= x:
            la = mid - 1
        else:
            st = mid + 1
    while st2 < la2:
        mid2 = (st2+la2) // 2
        if L[mid2] > x:
            la2 = mid2 - 1
        else:
            st2 = mid2 + 1
    # print(st, st2)
    if st2 - st == 0:
        print(ans)
    else:
        print(st2- st)
