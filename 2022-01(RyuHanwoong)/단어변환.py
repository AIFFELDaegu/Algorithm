als=[0]
def recursive_1(begin,target,words) :
    for i in range(len(begin)) :
        confirm = list(begin.replace(begin[i], ""))
        for word in words :
            if len( [con for con in confirm if con in word])==2:
                if(word==target):
                    print(word)
                    return True
                tmp = words.copy()
                tmp.remove(word)
                if recursive_1(word,target,tmp) :
                    print('a')
                    als[0]+=1
                    return True
                    
def solution_1(begin, target, words):
    answer = 0
    recursive_1(begin,target,words)
    if(als[0]):
        als[0]-=1
    return als[0]

def bfs(begin,target,words):
    queue =[begin]
    depth =0
    while queue :
        print(queue)
        begin_sentence = queue[0]
        for tmp in queue :
            if tmp in words :
                words.remove(tmp)
        queue.remove(begin_sentence)
        for i in range(len(begin_sentence)):
            print(begin_sentence)
            confirm = list(begin_sentence.replace(begin_sentence[i], ""))
            print(confirm)
            for word in words :
                if len([con for con in confirm if con in word])==2: 
                    if word==target :
                        return depth
                    queue.append(word)
        depth+=1
    return 0

def checkdiff1(query, key):
    diff = 0
    for a,b in zip(query,key):
        if a != b:
            diff += 1 
    return diff == 1 

def bfs_2(begin,target,words):
    queue =[begin]
    depth =0
    while queue :
        print(queue)
        
        for tmp in queue : #queue안의 단어와 words가 같으면 삭제
            if tmp in words :
                words.remove(tmp)
        queue_tmp=[]
        for begin_sentence in queue : #queue를 싹돌기
            for word in words :
                if checkdiff1(begin_sentence, word): 
                    if word==target :
                        return depth+1
                    queue_tmp.append(word)
        queue= queue_tmp 
        depth+=1
    return 0
                        
    
def solution(begin, target, words):
    answer = 0
    return  bfs_2(begin,target,words)