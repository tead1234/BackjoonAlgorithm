def solution(food_times, k):
    le = len(food_times)
    answer = 0
    k += 1
    num = 0
    passindex = []
    min_val = min(food_times)
    while k - (le * min_val) >=0:
        k -= (le * min_val)
        num = 0
        for i in range(le):
            food_times[i] -= min_val
            if food_times[i] < min_val and food_times[i] >0:
                min_val = food_times[i]
            elif food_times[i] <= 0:
                num += 1


        le -= 1

    print(k, le, min_val)
    return answer

print(solution(	[3, 1, 2], 5))
print(solution(	[1, 1, 1], 5))
print(solution(	[1, 100, 211], 5))
