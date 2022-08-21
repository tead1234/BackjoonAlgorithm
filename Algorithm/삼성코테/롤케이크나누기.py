def solution(topping):
    answer = 0
    L = len(topping)
    if L == 0:
        return answer
    ## 계속하는걸 줄여야 한다...
    ## set을 한번더 돌리는게 시간초과를 내는거같다
    ## i번째 숫자가 형배열에 없던거면 가짓수추가
    ## i번째 숫자가 동생배열에 중복으로 있는거면 가짓수는 그대로
    ## 중복이 아니면 가짓수 -1
    형 = {}
    A = 0
    동생 = {}

    for i in topping:
        if i in 동생.keys():
            동생[i] += 1
        else:
            동생[i] = 1
    B = len(set(topping))
    for a in topping:
        if a in 형.keys():
            형[a] += 1
            동생[a] -= 1
            if 동생[a] == 0:
                del 동생[a]
                B -= 1

        else:
            형[a] = 1
            A += 1
            동생[a] -= 1
            if 동생[a] == 0:
                del 동생[a]
                B -= 1
        if A == B:
            answer += 1

    return answer
## 딕셔너리로 푸는거 맞네
print(solution([1,2,3,1,4]))