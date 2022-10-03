from typing import List


def find2(a):
    b = 1
    c = 2
    while a > b:
        b *= c
    return b


def solution(queries: List[List[int]]) -> int:
    answer = 0
    # 0번째배열 리스트는 안씀
    ansList = {}
    ## 배열 숫자, 크기, 원소수
    for querie in queries:

        ## 배열 숫자, 원소수
        a, b = querie
        if a not in ansList.keys():
            c = find2(b)
            ansList[a] = [c, b]

        ## 만약에 있다면
        else:
            ##  크기 , 원소수
            l, q = ansList[a]
            if l < q + b:
                answer += q
                l = find2(q + b)
                ansList[a] = [l, q + b]
            else:
                ansList[a] = [l,q+b]
    return answer
print(solution([[2, 10], [7, 1], [2, 5], [2, 9], [7, 32]]))
print(solution(
[[1, 1], [1, 2], [1, 4], [1, 8]]))