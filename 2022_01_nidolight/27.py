#https://deok2kim.tistory.com/122

def solution(distance, rocks, n):
    answer = 0
    left = 1
    right = distance+1
    rocks.sort()
    while left < right:
        mid = (left+right)//2
        removed_rocks = 0
        cur_point = 0

        # 각 돌을 돌면서 제거할 돌을 찾는다
        for rock in rocks + [distance]:
            if rock - cur_point < mid:
                removed_rocks += 1
            else:
                cur_point = rock

        # 제거한 개수가 기준 보다 많으면 , 제거를 줄여야함
        # 바위 사이 최소거리 기준을 낮춰야 한다
        if removed_rocks < n+1:
            left = mid + 1

        # 제거한 개수가 기존 보다 적으면, 더 많은 바위를 제거해야함
        # 바위 사이 기준을 높여야 한다
        else:
            right = mid
    answer = left-1
    return answer

print(solution(25,[2, 14, 11, 21, 17],2))