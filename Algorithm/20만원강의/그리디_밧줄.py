ans = []
n = int(input())
## 반복문 2개를 돌릴 필요가 없다면 << 이미 정렬되고 리스트중에 하나씩만 찾아도 된다면
## key값을 선언해서  + 1 타겟을 정해서 해결한다. >> 이중 반복문 회피용용
A = [int(input()) for _ in range(n)]
print(A)
A = sorted(A)
for a in A:
	ans.append(a * n)
	n -= 1
print(max(ans))