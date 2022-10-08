from collections import deque

def insert(A):
    for i in range(1,len(A)):
        j = i
        while j > 0 and A[j-1] > A[j]:
            A[j-1], A[j] = A[j], A[j-1]
            j -= 1
    return A
def getMinimumHealth(initial_players, new_players, rank):
    # Write your code here
    # 스트렝스별로 리스트를 만들어서 다 모아놓기
    # 설마 그냐ㅐㅇ 순서대로 하는건가??
    strength = {}
    ans = 0
    new = deque(new_players)
    ans += initial_players[-rank]
    while new:
        initial_players.append(new.popleft())
        ans += insert(initial_players)[-rank]

    print(ans)

getMinimumHealth([1
,2
,5], [2,
5,
4
], 3)

