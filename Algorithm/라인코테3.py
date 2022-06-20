def solution(sentences, n):
    for 문장 in sentences:
        ## 알파벳을 다 센다음 가장 빈도가 높은 애들만 가져오면??
        ## 근데 반드시 최고점이 된다는 보장이 없음
        문장 = set(문장.replace(' ',''))
        ## 지금 문장은 각 알파벳별로 나눠짐



print(solution(["line in line", "LINE", "in lion"],5))

## line 4
## linek 5
## REBN 8
## lib 3
## liea
#PO 4
## n에서 최고 높은 점수를 받는 방법은 8일것
# 최고 점수 >> 가장많이 겹치는 알파벳으로 새우기
## 알파벳 갯수에 따라 몇개가 완성되는지로 판단하면 되려나??
## 각 단어의 알파벳 개수를 새고 알파벳 갯수제한이 들어오면 그 수