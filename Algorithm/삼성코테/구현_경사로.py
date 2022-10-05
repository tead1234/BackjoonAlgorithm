import sys
from collections import deque
sys.stdin = open("test.txt",mode='r')

N,L = map(int,sys.stdin.readline().split())
MAP = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
# 한줄씩 들고오기
def find(A):
    cnt = 0
    test = deque()
    ## 설치된 경사로 인덱스
    installed = []
    pivot = A[0]

        # 다른수가 나올때 까지 q에 저장
    for idx,a in enumerate(A):
        # a가 더 큰경우 같은경우
        if a == pivot:
            test.append(idx)
            print(test)
        elif a == pivot + 1:
            # 기준보다 1키면 저장된 수와
            if len(test) >=  L:
                for _ in range(L):
                    t = test.pop()
                    if t in installed:
                        return False
                    print(t)
                    installed.append(t)
                test.clear()
                pivot = a
                test.append(idx)
            else:
                return False
        elif a+1 == pivot:
            # a 쪽에 있는 애들의 갯수를 구해야됨
            test2 = deque()
            for o in range(idx,N):
                if a == A[o]:
                    test2.append(o)
                else:
                    break
            if len(test2) >=  L:
                for _ in range(L):
                    t = test2.popleft()
                    if t in installed:
                        return False
                    print(t)
                    installed.append(t)
                test.clear()
                test2.clear()
                pivot = a

        else:
            return False


    return True
# 가로줄
answer = 0
for m in MAP:
    if find(m):
        print(m)
        answer += 1
List = []
for k in range(N):
    for j in range(N):
        List.append(MAP[j][k])
    # LIST를 가지고따지기
    if find(List):
        print(List)
        answer += 1
    List = []

print(answer)
