import math

def solution(brown, yellow):
    answer = []
    a = math.floor(math.sqrt(yellow))

    for i in range(1, yellow+1):
        if (yellow) % i == 0:
            a = yellow//i
            b = yellow//a
            if brown == (b + 2) * 2 + (a * 2):
                answer.append(b+2)
                answer.append(a+2)
                break
    answer.sort(reverse=True)
    return answer

