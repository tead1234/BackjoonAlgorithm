from collections import Counter


# 피로도 최소화
## 그리드 or bfs
## 철다철철돌다 철, 돌만 잇을때
## 한 광물을 뭐로 깰지 선택할떄 반드지 현재 가장 적은 피로도가 전체의 최소 피로도를 보장하지 않음
## 반드시 다캘 필요가 없네
def solution(picks, minerals):
    dia = picks[0]
    iron = picks[1]
    stone = picks[2]
    answer = 0
    len(minerals) // 5
    cnt = 0
    ans = []
    ins = [0, 0, 0]
    for i in range(len(minerals)):
        cnt += 1
        if minerals[i] == "diamond":
            ins[0] += 1
        elif minerals[i] == "iron":
            ins[1] += 1
        elif minerals[i] == "stone":
            ins[2] += 1

        if cnt == 5:
            cnt = 0
            ans.append(ins)
            ins = [0, 0, 0]
    # if len(ins) != 0:
    #     ans.append(ins)
    ## 5개가 채워진 애들만 우선으로
    ans = sorted(ans, key=lambda x: (-x[0], -x[1], -x[2]))
    ## 각 배열마다 피로도 계산
    for a in ans:
        if picks[0] != 0:
            picks[0] -= 1
            answer += 5
        elif picks[1] != 0:
            picks[1] -= 1
            for i in range(3):
                if i == 0:
                    answer += (a[i] * 5)
                if i == 1:
                    answer += (a[i] * 1)
                if i == 2:
                    answer += (a[i] * 1)
        elif picks[2] != 0:
            picks[2] -= 1
            for i in range(3):
                if i == 0:
                    answer += (a[i] * 25)
                if i == 1:
                    answer += (a[i] * 5)
                if i == 2:
                    answer += (a[i] * 1)


    print(answer)
solution([0,1,1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"])