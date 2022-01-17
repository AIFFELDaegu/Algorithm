def compress(s,size):
    result = ''
    tmp = s[0:size]
    count = 1
    skip = 0

    for k in range(len(s)):
        if tmp != s[k+size:k+2*size]:
                tmp = s[k:k+size]
                
        if skip == 0:
            if tmp == s[k+size:k+2*size]:
                count += 1
                result += str(count) + tmp
                skip = size*count-1
            else:
                result += s[k]
            # print(k, tmp, s[k+size:k+2*size], skip,result)
                            
        else:
            count = 1
            skip -= 1
            tmp = s[k:k+size]
            # print(k, tmp,s[k+size:k+2*size],skip,result,'skip')
            continue

    return result


def solution(s):
    return min(list(map(lambda i: compress(s, i), range(1, len(s)))))


ans = compress("abcabcabcdedededed", 3)
print('\nans:', ans)

# print(solution("ababcdcdababcdcd"))
