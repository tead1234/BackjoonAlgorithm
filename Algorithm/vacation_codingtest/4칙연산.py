## dp
def solution(N, number):
    d = [[] for _ in range(9)]
    d[1] = [N]
    d[2] = list(set([1, N * N, 2 * N, 0, int(str(N)+str(N))]))
    ## N을 3개 가지고 만들수 있는 수는
    ## 1개를 가지고 만든 여러 숫자와 2개를 가지고 만든 여러 숫자들을 가지고 사직연산을 다해보면 된다.
    if N == number:
        return 1
    if number in d[2]:
        answer = 2
        return answer
    i = 3
    while True:
        if i > 8:
            return -1

        for k in range(1,i):
            L = d[k]
            L2 = d[i-k]


            for a in L:
                minus1 = 0
                minus2 = 0
                sli = 0
                sli2 = 0
                for b in L2:
                    plus = a + b
                    if a - b > 0:
                        minus1 = a - b
                    if b - a > 0:
                        minus2 = b - a
                    if a != 0 and b % a == 0:
                        sli = b // a
                    if b != 0 and a % b == 0:
                        sli2 = a // b
                    mul = a * b

                    if number in [plus, minus1, minus2, sli, sli2, mul,int(str(N) * i)]:
                        return i

                    else:
                        d[i].append(plus)
                        d[i].append(mul)
                        d[i].append(int(str(N) * i))

                        if minus1 >0:
                            d[i].append(minus1)
                        if minus2 >0 :
                            d[i].append(minus2)
                        if sli != 0:
                            d[i].append(sli)
                        if sli2 != 0:
                            d[i].append(sli2)
            d[i] = list(set(d[i]))
        i += 1

print(solution(5, 31168))