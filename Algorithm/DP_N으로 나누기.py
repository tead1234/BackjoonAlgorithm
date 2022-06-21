## N이 몇개 사용 됐을때 나올 수 있는 모든 수를 계산하면 된다.

def find(li1, li2,st, N):
    li3 = [int(str(N)*st)]
    div = 0
    div2 = 0
    for i in range(len(li1)):
        for j in range(len(li2)):
            ## 더하기
            sum = li1[i] + li2[j]
            li3.append(sum)
            ## 빼기
            minus = li1[i] - li2[j]
            li3.append(minus)
            minus2 = li2[j] - li1[i]
            li3.append(minus2)

            ## 곱
            mul = li1[i] * li2[j]
            # mul2 = li2[j] * li1[i]
            li3.append(mul)
            # li3.append(mul2)
            ## 나누기
            if li2[j] != 0:
                div = li1[i] // li2[j]
            if li1[i] != 0:
                div2 = li2[j] // li1[i]
            li3.append(div)
            li3.append(div2)
    li3 = list(set(li3))
    return li3


def solution(N, number):
    answer = 0
    d = [[0] for i in range(1000)]
    if N == number:
        return 1
    d[1] = [N]
    d[2] = [N*N, N//N, N+N, N-N]
    if number in d[2]:
        return 2
    for i in range(2, number):
        if i > 8 :
            return -1
        for j in range(1,i+ 1):
            ## 두 리스트에서 만들수 있는 모든 조합을 찾아야함
            d[i] = find(d[i-j], d[j],i, N)
            if number in d[i]:
                return i





print(solution(2,11))