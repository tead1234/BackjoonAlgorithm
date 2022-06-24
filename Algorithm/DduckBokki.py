import sys
N,M = map(int,input().split())


dduck_list = list(map(int,input().split()))

dduck_list = sorted(dduck_list)
# 높이 M으로 절단 START 는 무조건 0, end는 N -1
mid = (N//2) -1
MID = dduck_list[mid]
START = dduck_list[0]
END = dduck_list[N-1]
def binary(dduck_list,START,END,M,MID):
    total = 0
    while START <= END:
        for i in range(N):
            a = dduck_list[i] - MID
            if a >= 0:
                total += a
            else:
                pass
        if total == M:
            total = 0
            return MID

        elif total > M:
            START = MID+1
            binary(dduck_list,START,END,M,MID)
        elif total < M:
            END = MID-1
            binary(dduck_list, START,END,M,MID)
    else:
        print("답없음")
        return
print(binary(dduck_list,START,END,M,MID))

