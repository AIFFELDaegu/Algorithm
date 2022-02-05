from collections import deque

def solution(n,computers):
    answer = 0
    visited = [0]*n

    for i in range(n):
        if visited[i]:
            continue

        answer += 1
        dq = deque([computers[i]])
        while dq:
            nodes = dq.popleft()
            for j in range(n):
                if nodes[j] and not visited[j]:
                    dq.append(computers[j])
                    visited[j] = 1
                    
    return answer

    
print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))


'''
BFS
첫 번째 컴퓨터를 루트 노드로 두고, 연결된 컴퓨터들을 BFS로 탐색한다.
탐색 할 때, 지나간 노드를 visited에 표시한다.
탐색이 끝나면, visited를 이용하여 지나가지 않은 노드를 루트 노드로 만든다.
모든 노드에 대해서 탐색이 끝나면, BFS로 탐색을 시작한 횟수를 리턴한다.
'''