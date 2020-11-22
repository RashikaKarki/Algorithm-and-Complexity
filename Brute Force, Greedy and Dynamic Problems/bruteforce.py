def get_strings(n):
    liststring = []
    for x in range(2**n):
        if len("{0:b}".format(x)) != n:
            liststring.append(((n - len("{0:b}".format(x))) *'0') + "{0:b}".format(x))
        else:
            liststring.append("{0:b}".format(x))
    return liststring

def bruteforce(p, w, m):
    if len(p) == len(w):
        n = len(p)
        bit_strings = get_strings(n)
        max_profit = 0
        for s in bit_strings:
            profit = sum([int(s[i]) * p[i] for i in range(n)])
            weight = sum([int(s[i]) * w[i] for i in range(n)])
            if weight <= m and profit > max_profit:
                max_profit = profit
        return max_profit
    else:
        raise Exception("The list should be of same size")


def bruteforcefractional(p, w, c):
    if len(p) == len(w):
        n = len(p)
        maxProfit = 0
        bit_strings = get_strings(n)
        for b in bit_strings:
            i1 = [i for i,x in enumerate(b) if x == '1']
            i0 = [i for i,x in enumerate(b) if x == '0']
            nprofit = 0
            weight = 0
            for i in i1:
                nprofit += p[i]
                weight += w[i]
            fractionProfit = 0
            newB = b
            if weight < c :
                maxI = 0
                for i in i0:
                    r = (w[i], c - weight )[(c - weight < w[i])] 
                    f = (p[i]/w[i])*r
                    if f > fractionProfit:
                        fractionProfit = f
                        maxI = i 
            totalProfit = fractionProfit + nprofit
            if weight <= c and totalProfit >= maxProfit:
                maxProfit = totalProfit
        return maxProfit
    else:
        raise Exception("The list should be of same size")


