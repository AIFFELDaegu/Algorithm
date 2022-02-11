def solution(num, k):
    for _ in range(k):#k번 반복
        index = 0
        while(True):
            if index+1 == len(num) or num[index] < num[index+1]: 
                num = num[:index] + num[index+1:]
                break
            index += 1
    return num

print(solution("4177252841", 4))

''' # 중복스킵, test10만 실패
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

# def solution(number, k):
#     st = []
#     for i in range(len(number)):
#         print(st,number[i])
#         while st and k > 0 and st[-1] < number[i]:
#             st.pop()
#             k -= 1
#         st.append(number[i])
#     return ''.join(st[:len(st) - k])