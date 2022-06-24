import sys

count = 0
beforelist = []
afterlist = []
timeList = []

for line in sys.stdin:

    enterList = list(line.split())
    if len(enterList) == 3:
        timeList = enterList

    else:
        if enterList[0] <= timeList[0]:
            if enterList[1] in beforelist:
                continue
            beforelist.append(enterList[1])
        if timeList[1] <= enterList[0] <= timeList[2]:
            if enterList[1] in afterlist:
                continue
            afterlist.append(enterList[1])
print(afterlist)


# 중복제거 해야됨

# 개총 끝나고 채팅, 스트리밍 끝나고 채팅
