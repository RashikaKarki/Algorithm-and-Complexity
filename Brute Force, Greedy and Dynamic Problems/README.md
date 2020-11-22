# Brute Force, Greedy and Dynamic Problems

### Solving Knapsack problem using different algorithm design strategies such as:

- **Brute-force method**


Pseudo Code

```
bruteforce(p, w, c):
    if p and w length is same:
        n = len(w)
    else:
        throw error
    bit_strings = List of bitstrings of int n
    for s in bit_strings:
            profit = add all bit multiplied with value 
            weight = add all bit multiplied with weight
            if weight <= c and profit > sol:
                sol = profit
        return sol
```

```
bruteforcefractional(p, w, c):
    if len(p) == len(w):
        n = len(p)
    else:
        throw error
    let maxProfit = 0
    let bit_strings = List of bitstrings of int n
    while b in bit_strings:
        do i1 = [i for i,x in enumerate(b) if x == '1']
        do i0 = [i for i,x in enumerate(b) if x == '0']
        let nonfracprofit = 0
        let weight = 0
        while  i in i1:
            let nonfracprofit += p[i]
            let weight += w[i]
        let fractionProfit = 0
        let newB = b
        if weight < c then
            let maxI = 0
            while i is in i0:
                let r = (w[i], c - weight )[(c - weight < w[i])] 
                let f = (p[i]/w[i])*r
                if f > fractionProfit then
                    let fractionProfit = f
                    let maxI = i 
        let totalProfit = fractionProfit + nonfracprofit
        if weight <= c and totalProfit >= maxProfit then
            let maxProfit = totalProfit
    return maxProfit
```
- **Greedy method**


Pseudo Code

```
greedy(p, w, c)
    for i = 1 to n 
        do x[i] = 0 
    weight = 0 
    for i = 1 to n 
        if weight + w[i] ≤ W then  
            x[i] = 1 
            weight = weight + w[i] 
        else 
            x[i] = (W - weight) / w[i] 
            weight = W 
            break 
    return x
```

- **Dynamic programming**


Pseudo Code

```
Dynamic-0-1-knapsack (p, w, W):
    n = len(p)
    for w = 0 to W do 
        c[0, w] = 0 
    for i = 1 to n do 
        c[i, 0] = 0 
    for w = 1 to W do 
        if wi ≤ w then 
            if vi + c[i-1, w-wi] then 
                c[i, w] = p[i] + c[i-1, w-wi] 
            else c[i, w] = c[i-1, w] 
        else 
            c[i, w] = c[i-1, w] 
```

Test:
![Tests](https://github.com/RashikaKarki/Algorithm-and-Complexity/blob/master/Brute%20Force%2C%20Greedy%20and%20Dynamic%20Problems/tests.PNG)
