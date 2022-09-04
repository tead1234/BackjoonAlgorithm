T = int(input())
answer = []

# def dfs(start):
#     global Pass
#     S[start] = 'x'
#     if start - 1 >= 0:
#         if S[start - 1] != 'x':
#             if S[start - 1] == '1':
#                 S[start - 1] = '0'
#             elif S[start - 1] == '0':
#                 S[start - 1] = '1'
#     if start + 1 < len(S):
#         if S[start + 1] != 'x':
#             if S[start + 1] == '1':
#                 S[start + 1] = '0'
#             elif S[start + 1] == '0':
#                 S[start + 1] = '1'
#     for i in range(len(S)):
#         if S[i] == '1':
#             dfs(i)
#             if Pass:
#                 return
#     if '1' not in S:
#         if '0' not in S:
#             Pass = True
#     if Pass == False:
#         S[start] = '1'
#         if start - 1 >= 0:
#             if S[start - 1] != 'x':
#                 if S[start - 1] == '0':
#                     S[start - 1] = '1'
#                 elif S[start - 1] == '1':
#                     S[start - 1] = '0'
#         if start + 1 < len(S):
#             if S[start + 1] != 'x':
#                 if S[start + 1] == '0':
#                     S[start + 1] = '1'
#                 elif S[start + 1] == '1':
#                     S[start + 1] = '0'

for test_case in range(1, T + 1):
    S = list(input())
    Pass = False
    num1 = 0
    # for i in range(len(S)):
    #     if S[i] == '1':
    #         dfs(i)
    for s in S:
        if s == '1':
            num1 += 1
    if num1 %2 !=0:
        Pass = True

    if Pass:
        answer.append('#{} yes'.format(test_case))
        Pass = False
        # print('#{} yes'.format(test_case))
    else:
        answer.append('#{} no'.format(test_case))
        # print('#{} no'.format(test_case))
for a in answer:
    print(a)