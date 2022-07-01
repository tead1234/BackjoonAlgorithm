def valid(i,date,checked,N):
    ## 주어진 키값부터 date를 더한값이 N이하여야하고 checked의 범위안에도 False여야함
    if (i+date) > N:
        return False
    elif True in checked[i:i+date]:
        return False
    return True

def find_max(list):
    max = 0
    max_date = 0
    key = 0
    for i in range(len(list)):
        date, val  = list[i]
        if val > max:
            max = val
            max_date = date
            key = i
        elif val == max:
            if max_date > date:
                max_date = date
                key = i
    return key


N = int(input())

answer = 0
checked = [False] * N
i = 0
a = 0
input_list = [list(map(int, input().split())) for _ in range(N)]

while True:
    a += 1
    i = find_max(input_list)
    date = input_list[i][0]
    if valid(i,date,checked, N):
        for k in range(i,i+date):
            checked[k] = True
        answer += input_list[i][1]
        input_list[i] = [-1, -1]
    elif valid(i,date,checked, N) == False:
        input_list[i] = [-1, -1]
    if a > N:
        break

print(answer)
