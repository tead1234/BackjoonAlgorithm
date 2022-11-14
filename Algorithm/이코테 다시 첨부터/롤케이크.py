## 한번에 코딩하면 햇갈리고 피곤하니깐 부분으로 나누자
from collections import Counter
## 한번에 코딩하면 햇갈리고 피곤하니깐 부분으로 나누자

def solution(topping):
    bro = Counter(topping)
    young = set()
    ans = 0
    while len(topping)>1:
        q = topping.pop()
        young.add(q)
        if bro[q] > 1:
            bro[q] -= 1
        else:
            del bro[q]
        if len(bro) == len(young):
            ans += 1
    return ans

# print(numofKind([1,3,4,5]))
print(solution([1, 2, 1, 3, 1, 4, 1, 2]))