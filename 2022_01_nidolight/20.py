# def solution(name):
#     answer = 0
#     name = list(map(ord,name))
#     name = [13-abs(n-78) for n in name]

#     idx, answer = 0, 0
#     while True:
#         answer += name[idx]
#         name[idx] = 0
#         if sum(name) == 0:
#             break
#         left, right = 1, 1
#         while name[idx - left] == 0:
#             left += 1
#         while name[idx + right] == 0:
#             right += 1
#         answer += left if left < right else right
#         idx += -left if left < right else right
#     return answer


#ord() A~N~Z : 65~78~90

#https://velog.io/@doeunllee/프로그래머스-42860번-조이스틱

def solution(name):
    answer = 0
    n = len(name)

    def alphabet_to_num(char): 
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        return num_char[ord(char) - ord('A')]

    for ch in name:      # 알파벳 cost 먼저 합산
        answer += alphabet_to_num(ch)

    move = n - 1
    for idx in range(n): # 좌우 커서 이동 cost 따로 계산
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, n - next_idx)
        move = min(move, idx + n - next_idx + distance)

    answer += move
    return answer

print(solution("AAABAAAAAB"))