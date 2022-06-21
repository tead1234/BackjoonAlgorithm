## 연속해서 문자열을 지우고 그중에서 가장큰 수와 가장 작은 수의 차이가 최소가 되도록 설계
## dfs 같은 걸로 풀면될거같은데
## 리스트에서 가장 큰수오 ㅏ가장 작은수의 차이를 뽑아내는 함수를 하나 만듬
## 리스트를 K만큼 잘라내서 보여주면 됨
from collections import deque
def find(A):
    B = A.copy()
    if len(B) < 2:
        return
    B = deque(sorted(B))

    return B.pop() - B.popleft()

def slice(A,k,K):
    B = A.copy()
    if k+K > len(B):
        return
    del B[k:k+K]
    return B
def solution(A, K):
    min_list = []
    # write your code in Python 3.6
    for i in range(len(A)):
        if slice(A,i,K) == None:
            continue
        test = slice(A,i,K)
        # print(test)
        if type(find(test)) == None:
            continue

        c = find(test)
        min_list.append(c)
        # print(min_list)
    return sorted(min_list)[0]
# slice([3,5,1,3,9,8],1,7)
solution([8, 8, 4, 3], 2)