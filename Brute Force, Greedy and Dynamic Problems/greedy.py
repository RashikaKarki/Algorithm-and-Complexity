class ItemValue: 
    def __init__(self, wt, val, ind): 
        self.wt = wt 
        self.val = val 
        self.ind = ind 
        self.cost = val // wt 
  
    def __lt__(self, other): 
        return self.cost < other.cost 

def greedy(p, wt, capacity):
    pw = []
    n = 0
    if len(p) == len(wt):
        n = len(p)
        ip = [] 
        for i in range(len(wt)): 
            ip.append(ItemValue(wt[i], p[i], i)) 
  
        # sorting items by pue 
        ip.sort(reverse=True) 
  
        totalValue = 0
        for i in ip: 
            curWt = int(i.wt) 
            curVal = int(i.val) 
            if capacity - curWt >= 0: 
                capacity -= curWt 
                totalValue += curVal 
            else: 
                fraction = capacity / curWt 
                totalValue += curVal * fraction 
                capacity = int(capacity - (curWt * fraction)) 
                break
        return totalValue 
    
    else:

        raise Exception("The list should be of same size")

