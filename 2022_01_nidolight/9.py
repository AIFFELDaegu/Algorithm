
# def solution(numbers):
#     answer=[]
    
#     for nums in permute(numbers):
#         tmp = ''
#         for n in nums:
#             tmp += str(n)
#         answer.append(tmp)

#     return max(answer)

# def permute(arr):
#     result = [arr[:]]
#     c = [0] * len(arr)
#     i = 0
#     while i < len(arr):
#         if c[i] < i:
#             if i % 2 == 0:
#                 arr[0], arr[i] = arr[i], arr[0]
#             else:
#                 arr[c[i]], arr[i] = arr[i], arr[c[i]]
#             result.append(arr[:])
#             c[i] += 1
#             i = 0
#         else:
#             c[i] = 0
#             i += 1
#     return result
    

def solution(numbers):
    numbers =[[i for j in range(2)] for i in numbers] # 바깥 for문을 뒤에
    for i in range(0,len(numbers)):
        numbers[i][1]=len(str(numbers[i][0]))
    # print(numbers)
    answer=''

    i=0
    while(len(numbers)!=0):
        tmp = []
        max_tmp = []

        for num in numbers:
            if num[1]>i:
                tmp.append(num)

        tmp_num=0
        for t in tmp:
            if t[0]>tmp_num:
                tmp_num = t[0]
                max_tmp = t
        print(max_tmp)
        
        answer+=str(max_tmp[0])
        numbers.remove(max_tmp)
        print(numbers)

        


  

    # for i,num in enumerate(numbers):
    #     num.append(len(i))
   


    answer=''
    

    return answer

#리스트 원소의 맨앞[0]에서부터 비교해서 제일 큰 원소 선택해서 append




(solution([6, 99, 2]))