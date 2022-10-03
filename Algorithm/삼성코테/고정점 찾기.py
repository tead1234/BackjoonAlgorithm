import sys
# sys.stdin = open("input.txt")

N = int(input())
L = list(map(int,input().split()))
st = 0
la = N
if L[st] == 0:
    print(st)
if L[la-1] == N- 1:
    print(la-1)
else:
    while st < la:
        mid = (st + la) // 2
        if L[mid] > mid:
            la = mid - 1
        elif L[mid] <= mid:
            st = mid + 1
        elif L[st] == st:

        # elif L[mid] == mid:
        #     print(m)
            print(st)
            break
## 내가 지금까지 짜본게 st를 움직이는거라ㅣ 자꾸 이렇게 나오네