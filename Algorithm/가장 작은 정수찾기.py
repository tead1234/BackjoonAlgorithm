from collections import deque

cnt = 0

def find(A):
    global cnt
    c = A[0]
    a =  c+ 1
    if a <= 0:
        cnt += 1
        return False

    if a in A:
        return False
    return True


def solution(A):
    A = sorted(A)
    A = list(set(A))
    length = len(A)
    de_Q = deque(A)

    while de_Q:
        if not find(de_Q):
            c = de_Q.popleft()
            continue
        if find(de_Q):
            print(de_Q.popleft() + 1)
            break
    if cnt == length:
        print(1)


solution([-1,-3])