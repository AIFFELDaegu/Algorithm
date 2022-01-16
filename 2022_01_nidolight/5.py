def compress(s,size):
    result = ''
    tmp = s[0:size]
    count = 1
    skip = 0

    for j in range(len(s)):
        print(j)
        pass

    return len(result)


def solution(s):
    return min(list(map(lambda i: compress(s, i), range(1, len(s)))))


ans = compress("abcabcabcdedededed", 3)
print('\nans:', ans)

# print(solution("ababcdcdababcdcd"))
