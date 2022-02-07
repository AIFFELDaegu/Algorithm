def solution(clothes):
    answer = 1
    root ={}

    for a,b in clothes:
        if b not in root:
            root[b] = 1
        else:
            root[b] += 1

    for v in root:
        answer *= root[v]+1

    return answer - 1


print(solution([["yellowhat", "headgear"], [
      "bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
