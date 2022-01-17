import numpy as np
import pandas as pd

def solution(board, moves):
    answer = 0
    basket = []
    index = np.arange(len(board))
    df = pd.DataFrame(board, index=index)

    for m in moves:
        for i, col in enumerate(df.loc[:,m-1]):
            if col!=0:
                basket.append(df.loc[i,m-1])
                df.loc[i,m-1] = 0
                break
        if len(basket)>1 and basket[-1] == basket[-2]: #같은거 붐
            basket = basket[:-2]
            answer += 2
        # print(df,basket,answer,'\n')

    return answer


solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],
[1,5,3,5,1,2,1,4]) 
