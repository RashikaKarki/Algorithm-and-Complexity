import matplotlib.pyplot as plt
from random import sample
from time import time
from random import choice

# Binary Search
def binary_search(data, left, right, target):
    if right >= left:
        middle = (right + left) // 2
        if data[middle] == target:
            return middle
        elif data[middle] < target:
            return binary_search(data, middle+1, right, target)
        else:
            return binary_search(data, left, middle-1, target)
    else:
        return -1

def plot_data(data):
    plt.plot(data["index"], data["elapsed"]["best"], c="green", label="Best Case")
    plt.plot(data["index"], data["elapsed"]["worst"], c="red", label="Worst Case")
    plt.legend()
    plt.show()

def main(data):
    for i in range(1000, 100001, 1000):
        d = sample(range(100000), i)
        d.sort()
        data['index'].append(i)

        # for best case
        middle = d[(i-1)//2]
        start = time()
        binary_search(d, 0, i-1, middle)
        elapsed = time() - start
        data['elapsed']["best"].append(elapsed)

        # for worst case
        start = time()
        index = binary_search(d, 0, i-1, -1)
        elapsed = time() - start
        data['elapsed']["worst"].append(elapsed)
    #plotting
    plot_data(data)

if __name__ == "__main__":
    data = {
    "index": [],
    "elapsed": {
        "best": [],
        "worst": [],
    }
    }
    main(data)
