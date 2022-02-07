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

def solution1(clothes):
    from collections import Counter
    from functools import reduce

    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
#카운터는 이름과 그 이름의 갯수를 구해줌
#리듀스는 누적값 계산할 때 유용

print(solution1([["yellowhat", "headgear"], [
      "bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))

