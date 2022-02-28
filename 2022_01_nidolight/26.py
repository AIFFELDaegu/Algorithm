def solution(n, times):
    # high 가장 비효율적으로 심사했을 때 걸리는 시간
    low = 0
    high = max(times) * n

    while low < high:
        mid = (low + high) // 2
        sum = 0
        for t in times:
            #sum : 모든 심사관들이 mid분 동안 심사한 사람의 수
            sum += (mid // t)

        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 적은 경우
        if sum < n:
            low = mid + 1
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 많거나 같은 경우
        if sum >= n:
            high = mid

    return low #low든 high든 결과는 동일


print(solution(6,[7, 10]))


