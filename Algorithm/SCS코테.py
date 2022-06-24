# 테스트 케이스 수
def check(배열):
    for i in range(len(배열)-1):
        if 배열[i] > 배열[i + 1]:
            return True
    return False

T = int(input())
for _ in range(T):
    N = int(input())
    배열 = list(map(int,input().split()))
    flag = True
    answer = 0


    while flag:
        if check(배열):
            if N%2 == 1:
                for i in range(int(N/2)):
                    ## 홀수 자리 정리
                   if 배열[2*i] > 배열[2*i +1]:
                        temp = 배열[2 * i]
                        배열[2 * i] = 배열[2 * i + 1]
                        배열[2 * i + 1] = temp

                for i in range(int(N/2)):
                   if 배열[2*i +1] > 배열[2*i + 2]:
                       temp2 = 배열[2*i +1]
                       배열[2*i +1] = 배열[2 * i + 2]
                       배열[2 * i + 2] = temp2
                answer += 1
            if N%2 == 0:
                for i in range(int(N/2)):
                    ## 홀수 자리 정리
                   if 배열[2*i] > 배열[2*i +1]:
                        temp = 배열[2 * i]
                        배열[2 * i] = 배열[2 * i + 1]
                        배열[2 * i + 1] = temp

                for i in range(int(N/2)-1):
                   if 배열[2*i +1] > 배열[2*i + 2]:
                       temp2 = 배열[2*i +1]
                       배열[2*i +1] = 배열[2 * i + 2]
                       배열[2 * i + 2] = temp2
                answer += 1
        elif check(배열) == False:
            flag = False

    print("#{}".format(_),answer)