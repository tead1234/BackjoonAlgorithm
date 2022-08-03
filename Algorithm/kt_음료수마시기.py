from collections import deque

갯수 = []
리터_칼로리_번호 = []
ans = []
mx_ans = 0


def dfs(z, 갯수, p):
    global mx_ans
    ## 리터, 칼로리_ 갯수
    a, b, a1 = z
    if p <= 0:
        ans.append(mx_ans)
        return
    else:
        p -= a
        갯수[a1] -= 1
        mx_ans += b
        ## 중복해도 되니깐 true체크할 필요가 없음
        for li in 리터_칼로리_번호:
            c, d, e = li
            if 갯수[e] <= 0:
                continue
            if 갯수[e] > 0 and p > 0:
                dfs(li, 갯수, p -c)
            갯수[e] = 갯수[e] + 1
            mx_ans -= d

    return


## 사용할수 있는 음료수들만 담는 배열
## 각 리터당 최대의 열량을 내는 애들을 우선 배치
def solution(list, p):
    global 리터_칼로리_번호
    global mx_ans
    ## dp문제 list는 각각 갯수, 리터, 열량으로 구성
    ## p만큼으로 만들수 있는 최대열량 배열을 만들고 p+1의 값은 남은 음료중에 가장 큰 값을 가진 애를 더하면 되나??
    ## 남은 음료수 배열,
    for i, v in enumerate(list):
        a, b, c = v
        갯수.append(a)
        리터_칼로리_번호.append((b, c, i))
    for z in 리터_칼로리_번호:
        dfs(z, 갯수, p)
        mx_ans = 0
    return max(ans)

# 15 , 2리터 남음 1 16 + 9999
# 5 + 4 +
print(solution([[1, 3, 5], [5, 1, 2], [1, 1, 1], [3, 2, 2], [10, 10, 9999]], 10))
