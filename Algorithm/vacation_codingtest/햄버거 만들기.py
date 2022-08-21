
def solution(ingredient):
    ## 배열이 들어왔을때 1231이 몇번이나 있는지 찾아라
    ## 투포인터로 풀수 있지 않을까
    ## 리스트 슬라이싱의 힘?
    answer = 0
    n = len(ingredient)
    N = 1
    while N != 0:
        N = 0
        for i in range(n - 3):
            if [1, 2, 3, 1] == ingredient[i:i + 4]:
                answer += 1
                del ingredient[i:i + 4]
                N = 1
    return answer
print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))