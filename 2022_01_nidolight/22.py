def solution(N, number):
    arr = [None] + [{int(str(N)*i)} for i in range(1, 9)]

    for i in range(1, 9):
        for j in range(1, i):
            for num1 in arr[j]:
                for num2 in arr[i-j]:
                    arr[i].add(num1 + num2)
                    arr[i].add(num1 - num2)
                    arr[i].add(num1 * num2)
                    if num2:  # 0이 아닌경우 나누기
                        arr[i].add(num1 // num2)

        if number in arr[i]:
            return i

    return -1


print(solution(5, 12))
#https://ljw538.tistory.com/72
