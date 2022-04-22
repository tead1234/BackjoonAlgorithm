from collections import deque
N = input()
t = 0
que = deque()
que2 = deque()
que3 = deque()
for i in range(int(N)):
    li = input().split()
    a = int(li[0])
    b = li[1]
    que.append(tuple((a,b)))
while(True):
    # 만일 que의 튜플중 a자리가 t와 같다면 que2에 추가한다
    # 여기서 i가 차량 번호이므로 번호도 같이 저장하는게 좋을듯
    for i in range(int(N)):
        if que[i][0] == t:
            que2.append(tuple((i,que[i][1])))
    # for j in range(len(que2)):
    #     # 자리 위치를 비교해서 하나씩 순서로 배정해줘야됨
    #     if que2[j][1]  == 'A':
    #         break
    # 알파벳순으로 정렬 완료
    que2 = sorted(que2,key=lambda x : x[1])
