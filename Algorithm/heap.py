from collections import deque
import heapq
## 야발 최소 작업길이 그다음 최소 대기 시간 이렇게 해봐야 하나
def solution(jobs):
    총시간 = 0
    총작업시간 = 0
    # 최소대기시간 = 9999
    ## 리스트에서 가장 먼저 시작하는 애를 첫번째로
    key = 0
    h = []
    for job in jobs:
        heapq.heappush(h,job)
    print(h)
    ## 이걸 돌리면 최소 대기시간을 가진놈을 찾아는 내는데 추가적으로 더해주는 건 안될듯
    while (len(q) != 0):
        for i in range(len(q)):
            t1, t2 = q[i]
            if (총시간 - t1) < 최소대기시간 and (총시간 - t1) >=0:
                ## 최소대기시간을 찾아내면 그놈을 총작업시간
                최소대기시간 = 총시간 - t1
                선택요소 = q[i]
                key = i

            elif (총시간 - t1) == 최소대기시간 and (총시간 - t1)>=0:
                a, b = 선택요소
                if t2 < b:
                    최소대기시간 = 총시간 - t1
                    선택요소 = q[i]
                    key = i

                else:
                    continue
        ## 최종선택된 놈을 q에서 제거하고 위 과정을 반복
        t1, t2 = 선택요소
        총시간 = 총시간 + t2
        총작업시간 += 최소대기시간 + t2
        q.remove(q[key])
        key = 0
        최소대기시간 = 9999
    answer = 총작업시간 / len(jobs)
    return answer

print(solution([[0, 10], [4, 10], [15, 2], [5, 11]]))