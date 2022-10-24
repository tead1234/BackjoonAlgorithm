def solution(s):
    answer = 0
    start_idx=0
    end_idx= 0
    for idx, start in enumerate(s):
        if start == 'a' or start == 'z':
            start_idx = idx
            for idx_end, end in enumerate(s):
                if (end == 'a' and start == 'z' and idx_end > start_idx) or (end == 'z' and start == 'a' and idx_end > start_idx):
                    if 'a' not in s[start_idx+1: idx_end] and 'z' not in s[start_idx+1: idx_end]:
                        answer += 1
                    break
                else:
                    continue

    return answer


print(solution(
"zabzczxa"))