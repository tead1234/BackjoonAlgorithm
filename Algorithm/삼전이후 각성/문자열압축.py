##  aaaabbbbcccaaa >> a4b4c3a3으로 압축
# n시간동안 해결완료
def solution(a):
    tar = a[0]
    cnt = 0
    answer = ""
    for idx in a:
        if idx == tar:
           cnt += 1
           tar = idx
        else:
            answer += (tar + str(cnt))
            cnt = 1
            tar = idx
    answer += (tar + str(cnt))
    print(answer)

solution("aaaabbbbcccaaa")



