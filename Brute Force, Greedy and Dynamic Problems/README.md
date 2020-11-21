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

- **Greedy method**


Pseudo Code

```
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
Dynamic-0-1-knapsack (v, w, W):
    for w = 0 to W do 
    c[0, w] = 0 
    for i = 1 to n do 
    c[i, 0] = 0 
    for w = 1 to W do 
        if wi ≤ w then 
            if vi + c[i-1, w-wi] then 
                c[i, w] = vi + c[i-1, w-wi] 
            else c[i, w] = c[i-1, w] 
        else 
            c[i, w] = c[i-1, w] 
```

Test:
![Tests](https://github.com/RashikaKarki/Algorithm-and-Complexity/blob/master/Brute-Force,-Greedy-and-Dynamic-Problems/test-run-ss.PNG)
