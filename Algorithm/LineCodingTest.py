def solution(logs):
    answer = 0
    arr = []
    for i in range(len(logs)):
        대상 = logs[i]
        ## 로그 길이 체크하고
        if len(list(대상)) < 100:
            listForCheck = 대상.split(" ")
            ## 형식확인
            if (len(listForCheck)==12):
                if listForCheck[0] == "team_name":
                    if listForCheck[3] == "application_name":
                        if listForCheck[6] == "error_level":
                            if listForCheck[9] == "message":
                                    # 특수문자 확인
                                    if all(chr.isalpha() for chr in listForCheck[2]):
                                        if all(chr.isalpha() for chr in listForCheck[5]):
                                            if all(chr.isalpha() for chr in listForCheck[8]):
                                                if all(chr.isalpha() for chr in listForCheck[11]):
                                                    print(listForCheck)
                                                    answer += 1
    return answer

print(solution(["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange", "no such file or directory", "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11", "team_name : recommend application_name : recommend error_level : info message : Success!", "   team_name : db application_name : dbtest error_level : info message : test", "team_name     : db application_name : dbtest error_level : info message : test", "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]))
