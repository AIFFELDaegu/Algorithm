
#dfs를 이용
#글자가 하나만 다른 단어들 추출해서 tmp로 pop
#저장된 tmp에서 words와 글자가 하나만 다른 단어들 추출
#word가 빌때까지 반복
#만들어진 result에서 target확인

def solution(begin, target, words):
    result = [[begin]]

    def recursive(result, words):
        # print("result: {}\nwords: {}\n".format(result,words))
        tmp = []
        for r in result[-1]:
            for w in words:
                if check(r, w):
                    tmp.append(w)
            for t in tmp:
                if t in words:
                    words.remove(t)
        result.append(tmp)

        if not words or not tmp:  # words가 비어있으면 종료
            return
        return recursive(result, words)

    recursive(result, words)

    for i, r in enumerate(result):
        if target in r:
            return i
    return 0


def check(str1, str2):  # 한 단어만 다른지 확인
    count = 0
    for i, c in enumerate(str1):
        if c == str2[i]:
            count += 1
    if count == len(str1)-1:
        return True
    return False


# print(solution("hot",	"dog",	["hot","dog"]))
print(solution("aoa", "aof", ["aob", "aoc", "aod", "aof", "aoe"]))
