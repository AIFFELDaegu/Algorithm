def solution(n, results):
    win = {x:set() for x in range(1, n+1)}
    lose = {x:set() for x in range(1, n+1)}

    for winner, loser in results:
        win[winner].add(loser)
        lose[loser].add(winner)
    
    for i in range(1, n+1):
        for winner in lose[i]:# i한테 진 애들은 i를 이긴 애들한테도 진 것
            win[winner].update(win[i])
        for loser in win[i]:  # i한테 이긴 애들은 i한테 진 애들한테도 이긴 것
            lose[loser].update(lose[i])

    answer = 0
    for i in range(1, n+1):   # i한테 이기고 진 애들 합쳐서 n-1이면 순위가 결정된 것
        if len(win[i]) + len(lose[i]) == n-1:
            answer += 1
    return answer


# 단방향 -> 인접리스트 2개
print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))


