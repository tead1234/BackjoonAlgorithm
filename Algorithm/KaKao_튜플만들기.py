def solution(s):
    answer = []
    mini = []
    answer_copy = []
    for i in range(len(s)):
        if s[i] == '{':
            start = i
        if s[i] == '}':
            end = i
            mini = s[start+1:end]
            answer_copy.append(mini)
            start = 0
            end = 0
    print(answer_copy)


        #
        # if i.isdigit():
        #     mini.append(i)
        # if i == '}' and len(mini) != 0:
        #     answer_copy.append(mini)
        #     mini = []
    answer_copy = sorted(answer_copy, key= len)
    ## 길이별로 정리됐으니 가장 처음부터 하나씩 비교하면서 더하면 됨
    for val in answer_copy:
        for x in val:
            if not x in answer and x != "":
                print(x)
                answer.append(x)
    return answer






solution("{{20,111},{111}}")
solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")