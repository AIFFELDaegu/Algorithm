from itertools import permutations

def solution(numbers):
    answer = 0
    numbers = list(numbers)

    per = []
    for i in range(1, len(numbers)+1):   
        per += list(permutations(numbers, i))    

    nums = [int(("").join(p)) for p in per]
    nums = set(nums)

    for n in nums:
        if is_prime_number(n):
            answer += 1
    return answer

def is_prime_number(x):
    if x == 1 or x ==0:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False 
    return True 

print(solution("17"))
