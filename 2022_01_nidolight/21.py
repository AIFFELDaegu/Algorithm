# def solution(num, k):
#     for _ in range(k):#k번 반복
#         index = 0
#         while(True):
#             if index+1 == len(num) or num[index] < num[index+1]: 
#                 num = num[:index] + num[index+1:]
#                 break
#             index += 1
#     return num


''' # 중복스킵, test10 시간초과
def solution(num, k):
    switch = True
    for _ in range(k):#k번 반복
        if switch:
            index = 0
        else:
            index = tmp
            switch = True
        while(True):
            if index+1 == len(num) or num[index] < num[index+1]: 
                num = num[:index] + num[index+1:]
                break
            if num[index] == num[index+1]:
                switch = False
                tmp = index
            index += 1
    return num
'''

def solution(number, k):
    st = []
    for i in range(len(number)):
        while st and k > 0 and st[-1] < number[i]:
            st.pop()
            k -= 1
        st.append(number[i])
    # if k != 0:    #return에서 슬라이싱을 통해 구현
    #     stack = stack[:-k] 
    return ''.join(st[:len(st) - k])

print(solution("4177252841", 4))