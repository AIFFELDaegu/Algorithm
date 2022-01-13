
#        2 5 8 0
# 1 2 3  1 2 3 4
# 4 5 6  2 1 2 3
# 7 8 9  3 2 1 2
#-1 0-2  4 3 2 1

def solution(numbers, hand):
    answer = ""
    left_is = -1
    right_is = -2

    distances = {
        2: {
            1: 1, 4: 2, 7: 3, -1: 4,
            2: 0, 5: 1, 8: 2,  0: 3,
            3: 1, 6: 2, 9: 3, -2: 4
        },
        5: {
            1: 2, 4: 1, 7: 2, -1: 3,
            2: 1, 5: 0, 8: 1,  0: 2,
            3: 2, 6: 1, 9: 2, -2: 3
        },
        8: {
            1: 3, 4: 2, 7: 1, -1: 2,
            2: 2, 5: 1, 8: 0,  0: 1,
            3: 3, 6: 2, 9: 1, -2: 2
        },
        0: {
            1: 4, 4: 3, 7: 2, -1: 1,
            2: 3, 5: 2, 8: 1,  0: 0,
            3: 4, 6: 3, 9: 2, -2: 1
        }
    }

    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            left_is = n
        elif n in [3, 6, 9]:
            answer += 'R'
            right_is = n
        else:
            if distances[n][left_is] < distances[n][right_is]:
                answer += 'L'
                left_is = n
            elif distances[n][left_is] > distances[n][right_is]:
                answer += 'R'
                right_is = n
            elif hand == 'left':
                answer += 'L'
                left_is = n
            else:
                answer += 'R'
                right_is = n
        #print(n, answer)

    return answer

# def distance(hand, number):
#     keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
#     hand_coord, num_coord = None, None
#     for i in range(len(keypad)):
#         for j in range(len(keypad[0])):
#             if keypad[i][j] == hand:
#                 hand_coord = (i, j)
#             if keypad[i][j] == number:
#                 num_coord = (i, j)
#     return abs(hand_coord[0]-num_coord[0]) + abs(hand_coord[1]-num_coord[1])