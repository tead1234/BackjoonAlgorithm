# print("09:00" > "11:10")
from datetime import datetime, timedelta

def solution(plans):
    ## 24시간 넘어갈 수도 있음
    ## 다음 새 시간이 들어오기 전에 끝낼 수 있는지 없는지
    reserver = []
    plans.sort(key = lambda x : x[1])
    flg = 0
    for i in range( len(plans) -1 ):
        time_str1 = plans[i][1]
        time_str2 = plans[i+1][1]
        time1 = datetime.strptime(time_str1, %H:%M")
        time2 = datetime.strptime(time_str2, %H:%M")
        if time1 + timedelta(minutes = int(plans[i][2])) < time2:
            answer.append(plans[i][0])
            flg = time1 + timedelta(minutes = int(plans[i][2]))
        else:
            reserver.append([plans[i][0], time2 - time1 + timedelta(minutes = int(plans[i][2]))])
            flg = time2
        time_diff = time2 - time1

    answer = []


    return answer