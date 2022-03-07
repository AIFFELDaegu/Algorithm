answer=[]
def dfs(tikets,start) :
        dsts = []
        for tiket in tikets : #start 이후 갈 목적지 정렬
            if tiket[0] == start :
                dsts.append(tiket)
        dsts.sort()
        for dst in dsts :
            tmp = tikets.copy()
            tmp.remove(dst)  
            if dfs(tmp,dst[1]):
                answer.insert(0,dst[1])
                return True
            if not tmp :
                answer.append(dsts[0][1])
                return True 
        return False

def solution(tickets):
    dfs(tickets,"ICN")
    answer.insert(0,"ICN")
    return answer