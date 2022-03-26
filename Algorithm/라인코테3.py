def solution(sentences, n):
    for 문장 in sentences:

        문장 = set(문장.replace(' ',''))
        ## 지금 문장은 각 알파벳별로 나눠짐



print(solution(["line in line", "LINE", "in lion"],5))