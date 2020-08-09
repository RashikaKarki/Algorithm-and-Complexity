import matplotlib.pyplot as plt
import random
from time import time

def linear_search(d, target):
    for i in range(len(d)):
        if d[i] == target:
            return i
    return -1

def plot_data(data):
    plt.plot(data["index"], data["elapsed"]
         ["best"], c="green", label="Best Case")
    plt.plot(data["index"], data["elapsed"]
            ["worst"], c="red", label="Worst Case")
    plt.legend()
    plt.show()

def main(data):
    for i in range(1000, 100001, 1000):
        d = random.sample(range(100000), i)
        data['index'].append(i)

        # for best case
        start = time()
        linear_search(d, d[0])
        elapsed = time() - start
        data['elapsed']["best"].append(elapsed)

        # for worst case
        start = time()
        linear_search(d, -10000)
        elapsed = time() - start
        data['elapsed']["worst"].append(elapsed)

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

