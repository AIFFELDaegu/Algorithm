# def solution(prices):
#     answer = []

#     for i in range(len(prices)-1):
#         print(answer)
#         cnt = 0
#         for j in range(i, len(prices)-1):
#             if prices[i] <= prices[j]:
#                 cnt += 1
#             else:
#                 break
#         answer.append(cnt)
#     answer.append(0)
    
#     return answer

# def solution(prices):
#     answer = [0] * len(prices)
#     for i in range(len(prices)):
#         # print(answer)
#         for j in range(i+1, len(prices)):
#             if prices[i] <= prices[j]:
#                 answer[i] += 1
#             else:
#                 answer[i] += 1
#                 break
#     return answer

def solution(prices):
    n = len(prices)
    # 1. answer를 prices 길이와 맞춘다.
    answer = [0] * n
    # 2. 스택 생성
    st = []
    # 3. 0 ~ n-1 초까지 순회
    for i in range(n):
        # 1. 스택 비지 않고, prices[top] > prices[i] 이라면 다음 반복
        # 1-1. 스택에서 마지막에 저장된 시간 top 꺼냄
        # 1-2. answer[top]에 i - top을 저장
        while st and prices[st[-1]] > prices[i]:
            top = st.pop()
            answer[top] = i - top
        # 2. 스택에 현재 시간 i 저장
        st.append(i)
    
    # 4. 만약 스택이 남아있다면, 스택이 빌 때까지 다음 반복
    while st:
        # 1. 스택에서 마지막에 저장된 시간 top 꺼냄
        # 2. answer[top]에 가장 마지막 시간 n - i 에서 top을 뺸 시간 저장
        top = st.pop()
        answer[top] = n - 1 - top
    
    return answer


print(solution([10, 20, 30, 20, 30]))