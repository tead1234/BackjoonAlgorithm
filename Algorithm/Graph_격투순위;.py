def solution(n, results):
    answer = 0
    ## 결과가 N-1 개로 확정되는 애를 기준으로 곗간
    results_show = [0] * n
    results_final = [0] * n
    results_lose = [0] * n
    for res in results:
        a,b = res
        results_show[a - 1] += 1
        results_show[b - 1] += 1
        ## 진 횟수가 결국 자리수를 결정
        results_lose[b-1] += 1
    for i in range(len(results_show)):
        if results_show[i] == n-1:
            key = i
            lose = results_lose[key]
            results_final[lose] = key+1

    for j in range(len(results_final)):
        if results_final[j] != 0 and results_final[j] != n+1:
            answer+=1
            if j == 1:
                answer += 1
                results_final[0] = n+1

            if j >= 2 and results_final[j-1] == 0 and results_final[j-2] != 0:

                answer +=1
                results_final[j-1] = n+1
            if j >= 2 and j<=n-3 and results_final[j+1] == 0 and results_final[j+2] != 0:
                answer += 1
                results_final[j + 1] = n + 1
            elif j == n-2:
                answer += 1
                results_final[n-1] = n+1
    print(results_final)
    return answer




print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [1,4], [5,4]]))