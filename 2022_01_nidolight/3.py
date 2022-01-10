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
        if n == 1 or n == 4 or n == 7:
            answer += 'L'
            left_is = n
        elif n == 3 or n == 6 or n == 9:
            answer += 'R'
            right_is = n
        else:
            if distances[n][left_is] == distances[n][right_is]:
                if hand == 'left':
                    answer += 'L'
                    left_is = n
                else:
                    answer += 'R'
                    right_is = n
            elif distances[n][left_is] < distances[n][right_is]:
                answer += 'L'
                left_is = n
            elif distances[n][left_is] > distances[n][right_is]:
                answer += 'R'
                right_is = n
        #print(n, answer)

    return answer
