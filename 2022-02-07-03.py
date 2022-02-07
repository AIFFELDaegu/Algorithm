def solution(clothes):
    answer=1
    type_of_clothes = {i[1] : [] for i in clothes }
    for i in clothes :
        type_of_clothes[i[1]].append(i[0])
    tmp =[]
    for k in type_of_clothes.keys():
         tmp.append(len(type_of_clothes[k])+1)
    
    for i in tmp:
        answer*=i
    answer-=1
    return answer