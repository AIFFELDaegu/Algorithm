def solution(clothes):
    answer = 1
    dict = {}

    for a, b in clothes:
        if b not in dict:
            dict[b] = 1
        else:
            dict[b] += 1

    for v in dict:
        answer *= dict[v] + 1

    return answer - 1


print(solution([["yellowhat", "headgear"], [
      "bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
