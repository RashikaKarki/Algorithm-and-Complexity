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
        solution =''
        for s in bit_strings:
            profit = sum([int(s[i]) * p[i] for i in range(n)])
            weight = sum([int(s[i]) * w[i] for i in range(n)])

            if weight <= m and profit > max_profit:
                max_profit = profit
                solution = s
        return [solution, max_profit]
    else:
        raise Exception("The list should be of same size")


if __name__ == "__main__":
    p = [1,2,3]
    w = [4,5,1]
    m = 4

    bruteforce(p,w,m)

