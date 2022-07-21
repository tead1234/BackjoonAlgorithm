def bfs(list_a, i, checked):
    for j in range(len(list_a[i])):
        if list_a[i][j] in checked:
            continue
        if not list_a[i][j] in checked:
            checked.append(list_a[i][j])
            bfs(list_a, list_a[i][j]-1, checked)
    # print(checked)
    return checked
def bfs2(list_a, i, checked2):
    for j in range(len(list_a[i])):
        if list_a[i][j] in checked2:
            continue
        if not list_a[i][j] in checked2:
            checked2.append(list_a[i][j])
            bfs2(list_a, list_a[i][j]-1, checked2)
    # print(checked)
    return checked2

def solution(n, results):
    answer = 0
    checked = []
    checked2 = []
    ## 결과가 N-1 개로 확정되는 애를 기준으로 곗간
    results_lose = [[] for i in range(n)]
    results_win = [[] for i in range(n)]

    for res in results:
        ## a는 이긴놈 b는 진놈
        a,b = res
        results_lose[b - 1].append(a)
        results_win[a - 1].append(b)


    for i in range(len(results_win)):
        if not results_win[i]:
            pass
        copy = bfs(results_win, i , checked)
        results_win[i] = results_win[i] + copy
        results_win[i] = list(set(results_win[i]))
        checked = []
        if not results_lose[i]:
            pass
        copy2 = bfs2(results_lose, i, checked2)
        results_lose[i] += copy2
        results_lose[i] = list(set(results_lose[i]))
        checked2  = []
    ## 가장 많이 보이는 놈의 위치를 확정시키는게 중요
    results_fianl = list(map(list.__add__, results_win, results_lose))
    for a in results_fianl:
        if len(a) == n-1:
            answer+=1
    return answer




print(solution(4, [[1, 2], [1, 4], [2, 3], [1, 3]]))