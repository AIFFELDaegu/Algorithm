
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
    

def solution(num):
    
    num = list(map(str, num))
    num.sort(key = lambda x : x*3, reverse = True)
    
    return str(int(''.join(num)))



(solution([6, 99, 2]))
