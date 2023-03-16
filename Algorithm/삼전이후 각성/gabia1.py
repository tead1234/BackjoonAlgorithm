## 우선순위
## 앞 k의 순서가 바뀔때마다 +1
##
from collections import deque


def sort(List, a):
    name, score = a
    chek = False
    for i in range(len(List)):
        if List[i][1] < score:
            List.insert(i, (name, score))
            chek = True
            break
    if chek != True:
        List.append(a)
    return List


def solution(K, user_scores):
    answer = 0
    rank = []
    rank_name = []
    last = 0
    ## 첫 배열 만들기
    q = deque(user_scores)
    while q:
        if len(rank) == K:
            break
        name, score = q.popleft().split()
        if name in rank_name:
            index = rank_name.index(name)
            instance = []
            n, s = rank[index]
            print("index", index)
            if name == n and s < int(score):
                rank.remove((n, s))
                rank = sort(rank, (name, int(score)))
                for r in rank:
                    instance.append(r[0])
                if instance != rank_name:
                    answer += 1
                    rank_name = instance.copy()
        else:
            rank = sort(rank, (name, int(score)))
            for r in rank:
                rank_name.append(r[0])
    last = rank[-1][1]
    answer += K
    while q:
        name, score = q.popleft().split()
        if name in rank_name:
            index = rank_name.index(name)
            instance = []
            n, s = rank[index]
            if name == n and s < int(score):
                rank.remove((n, s))
                sort(rank, (name, int(score)))
                for r in rank:
                    instance.append(r[0])
                if instance != rank_name:
                    answer += 1
                rank_name = instance.copy()

            elif int(score) > last:
                answer += 1
                rank.pop()
                sort(rank, (name, int(score)))
                last = rank[-1][1]
                print(rank)
    return answer
A = [('cheries2', '200'), ('alex111', '100')]
print(solution(3, ))