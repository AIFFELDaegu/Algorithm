def solution(numbers, target):
    tree = [numbers[0]]
    answer = 0
    tree_i =0
    num_i = 1
    tmp =1
    n_len = len(numbers)
    while num_i<n_len :
        for i in range(0,tmp):
            tree.append(tree[tree_i] - numbers[num_i])
            tree.append(tree[tree_i] + numbers[num_i])
            tree_i+=1
        num_i+=1
        tmp*=2
        
    z= (1<<n_len-1)-1

    for i in range(z,len(tree)):
        if tree[i] == target or (tree[i]-2*numbers[0])==target: 
            answer+=1

            
    
    return answer