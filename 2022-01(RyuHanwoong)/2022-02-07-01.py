def solution(participant, completion):
    dictionary = dict.fromkeys(participant,0)
    answer=''
    for i in participant :
        dictionary[i]+=1
    for i in completion : 
        dictionary[i]-=1
    
    for k in dictionary.keys():
        if dictionary[k]!=0 :
            answer=k
    
    return answer