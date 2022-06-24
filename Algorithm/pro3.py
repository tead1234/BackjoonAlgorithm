def solution(answers):
    answer = []
    ### a,b,c
    a = 0
    a_list = [1,2,3,4,5]
    b = 0
    b_list = [ 2, 1, 2, 3, 2, 4, 2, 5,]
    c = 0
    c_list = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    res =0
    for i in range(len(answers)):
        if answers[i] == a_list[i%5]:
            a += 1
        if answers[i] == b_list[i%8]:
            b+=1
        if answers[i] == c_list[i%10]:
            c+=1
    res = max(a,b,c)
    if res == a:
        answer.append(1)
    if res == b:
        answer.append(2)
    if res == c:
        answer.append(3)
    answer.sort()
    return answer