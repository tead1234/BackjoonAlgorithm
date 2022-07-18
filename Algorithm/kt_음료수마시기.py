def minus(list):
    a, b, c = list
    list2 = [a - 1, b, c]
    return list2
def solution(list, p):
    ## dp문제 list는 각각 갯수, 리터, 열량으로 구성
    ## p만큼으로 만들수 있는 최대열량 배열을 만들고 p+1의 값은 남은 음료중에 가장 큰 값을 가진 애를 더하면 되나??
    ## 남은 음료수 배열,
    d = [0] * p
    ## mx_val = [갯수,리터,열량]
    mx_val = sorted(list, key= lambda x: x[2], reverse= True)
    d[0] = mx_val[0][2]
    mx_val[0] = minus(mx_val[0])
    d[1] =

print(solution([[1,3,5],[5,1,2]], 3))