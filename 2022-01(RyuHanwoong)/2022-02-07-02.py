def solution(phone_book):
    len_phone=[]
    phone_dic={}
    answer = True
    for i in phone_book :
        len_phone.append([len(i),i])
    
    len_phone.sort()
    
    for i in len_phone :
        phone_dic[i[1]] =0
    
    print(phone_dic.getkeys())
    for i in len_phone :
        for j in len_phone :
            if i[1]==j[1][0:i[0]] and i[1]!=j[1]:
                answer=False
    print(len_phone)
    
    return answer