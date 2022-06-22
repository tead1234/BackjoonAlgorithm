
def solution(record):
    answer = []
    임시리스트 = []
    dic = {}
    for red in record:
        # print(red)
        if "Enter" in red:
            red_Id = red.split()[1]
            red_Nick = red.split()[2]
            dic[red_Id] = red_Nick
            임시리스트.append([0,red_Id])
            # answer.append("{}님이 들어왔습니다.".format(red_Nick))
            # print(red1)
            # print(red)
        elif "Leave" in red:
            ## leave에선 id만 나오네
            red2 = red.split()[1]
            임시리스트.append([1,red2])

            # answer.append("{}님이 나갔습니다.".format(red_Leave))

        elif "Change" in red:
            ## answer 리스트를 찾은다음 그중에 id값으로 검색한다음 바꾸면 될듯
            red_change_id = red.split()[1]
            red_chaged_Nick = red.split()[2]
            dic[red_change_id] = red_chaged_Nick

    for a in 임시리스트:
        if a[0] == 0:
            answer.append("{}님이 들어왔습니다.".format(dic[a[1]]))
        if a[0] == 1:
            answer.append("{}님이 나갔습니다.".format(dic[a[1]]))


    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))