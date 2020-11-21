def dynamic(p, w, capacity): 
    if len(w) == len(p):
        n = len(p)
        K = [[0 for x in range(capacity + 1)] for x in range(n + 1)] 
    
        for i in range(n + 1): 
            for j in range(capacity + 1): 
                if i == 0 or w == 0: 
                    K[i][j] = 0
                elif w[i-1] <= j : 
                    K[i][j] = max(p[i-1] 
                            + K[i-1][j-w[i-1]],   
                                K[i-1][j]) 
                else: 
                    K[i][j] = K[i-1][j] 
    
        return K[n][capacity] 
   
    else:
        
        raise Exception("The list should be of same size")