from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)] # 연결된 노드 정보 그래프
    distance = [-1] * (n+1) # 각 노드의 최단거리 리스트

    for e in edge: 
        graph[e[0]].append(e[1]) 
        graph[e[1]].append(e[0])
    
    queue = deque([1]) # BFS를 위한 큐, 출발 노드는 1
    distance[1] = 0 # 출발 노드의 최단거리 0으로 
    # BFS 수행
    while queue:
        now = queue.popleft() # 현재 노드
        print(now,graph[now],distance)
        # 현재 노드에서 이동할 수 있는 모든 노드 확인
        for i in graph[now]:
            if distance[i] == -1: # 아직 방문하지 않은 노드라면
                queue.append(i) # 큐에 추가
                distance[i] = distance[now] + 1 # 최단거리 갱신
    
    # 가장 멀리 떨어진 노드 개수 구하기
    for d in distance:
        if d == max(distance):
            answer += 1

    return answer


# 인접행렬 -> 인접리스트(양방향)
print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))


