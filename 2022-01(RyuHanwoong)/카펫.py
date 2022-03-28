def solution(brown, yellow):
    #정사각형 확인
    answer= []
    total = brown+yellow 
    side = math.sqrt(total)
    if side%1 !=0 :
        #yellow의 최대 y를 구해야한다.
        #yellow가 짝수 홀수일 경우를 구분
        if yellow%2 :
            max_y = yellow/2 
        else :
            max_y =int(yellow/2)+1
            
        yellow_x = yellow 
        yellow_y = 1
        yellow_list = []
        while True :
            if max_y<yellow_y :
                break
            yellow_list.append([yellow_x,yellow_y])
            yellow_y+=1
            yellow_x=int(yellow/yellow_y)
        #이제 yellow에 맞는 brown의 x,y를 구해야한다.
        #brown은 yellow_x와 yellow_y보다 크고, x가 y보다 더 크면 ok
        #total을 구해서 각 yellow에 맞는 경우가 있는지 확인한다.
        x = int(total/3)
        y = 3
        switch =False
        while True :
            sum = x*y 
            if sum== total :
                for yel in yellow_list :
                    if x>yel[0]+1 and y>yel[1]+1 :
                        print(x,y,yel[0],yel[1])
                        switch=True
                if switch :
                    break
                    
            elif total<sum or y>x :
                x=int(total/3)+1
                y=3              
                break                        
            y+=1
            x=int(total/y)
        answer.append(x)
        answer.append(y)
    
         
    else :
        print("정사각형")
        answer.append(side)
        answer.append(side)
    return answer
    
