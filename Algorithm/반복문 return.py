def solive():
    for i in range(5):
        for j in range(5):
            if j == 3:
                return
            print(j)
# return을 쓰면 현재 함수를 종료시킬 수 있음 >> 계속 반복되는 재귀에서 특정부분만 종료 그리고 무조건 함수에서만 사용

def dis():
    for i in range(5):
        print(i)
        solive()

dis()



