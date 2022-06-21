## 일단 재택근무자들만 따로 빼고
## 팀별로 묶어서 재택근무만 있는 팀의 최소 번호인 사람만 빼면 되지않을까?
재택행렬 = []
출근행렬 = []
answer = []

def solution(num_teams, remote_tasks, office_tasks, employees):
    teams = [0] * num_teams
    teams2 = [0] *num_teams
    # emplyees를 리스트로 만들고 [1] 요소로 빼기 사원 번호는 i+1
    for person in employees:
        person_list = person.split()
        teams[int(person_list[0]) - 1] +=1
        for i in range(1,len(person_list)):
            if person_list[i] in office_tasks:
                출근행렬.append(person)
                continue

    for i in range(len(employees)):
        if not employees[i] in 출근행렬:
            재택행렬.append((employees[i],i+1))
    for 재택 in 재택행렬:
        재택정보 = 재택[0].split()
        teams2[int(재택정보[0]) - 1] += 1
    ## 겹치는 팀은 찾았는데
    for i in range(num_teams):
        if teams[i] == teams2[i]:
            ## 재택행렬을 가져오고
            for 재택 in 재택행렬:
                재택정보 = 재택[0].split()
                if int(재택정보[0]) == i+1:
                    재택행렬.remove(재택)
                    break
    for 재택 in 재택행렬:
        재택근무번호 = int(재택[1])
        answer.append(재택근무번호)
    ## 각 팀당 팀원수를 구하고 재택근무하는 애들 팀으로 묶어서 숫자 구하고 같으면 제일 낮은 수인놈 빼기

    return answer

print(solution(3,["development","marketing","hometask"],["recruitment","education","officetask"],["1 development hometask","1 recruitment marketing","2 hometask","2 development marketing hometask","3 marketing","3 officetask","3 development"]))