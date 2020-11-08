import random
import time
import math
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplot, figure

insert_time = []

merge_sort_time = []

size = []

def insertionsort(list):
        for index in range(1, len(list)):
                value = list[index]
                i = index - 1
                while i>=0:
                        if value < list[i]:
                                list[i+1] = list[i]
                                list[i] = value
                                i = i-1
                        else:
                                break
        return list

def mergesort(data,p,r):
        if(p<r):
                q = (p+r)//2
                data = mergesort(data,p,q)
                data = mergesort(data,q+1,r)
                data = merged(data,p,q,r)
        return data
        

def merged(data,p,q,r):
        L = data.copy()[p:q+1]
        R = data.copy()[q+1:r+1]
        L.append(math.inf)
        R.append(math.inf)
        i,j=0,0
        for k in range(p,r+1):
                if(L[i]<R[j]):
                        if(k<len(data)):
                                data[k] = L[i]
                                i+=1
                else:
                        if(k<len(data)):
                                data[k] = R[j]
                                j+=1
        return data

def insertion():
        for i in range(100,1000,10):
                list = random.sample(range(1000),i)
                start = time.time()
                sorted_list = insertionsort(list)
                end = time.time()
                t = end - start
                insert_time.append(t)
                size.append(i)

def merge():
        for i in range(100,1000,10):
                list = random.sample(range(1000),i)
                start = time.time()
                sorted_list = mergesort(list,0,len(list))
                end = time.time()
                t = end - start
                merge_sort_time.append(t)
        

insertion()
data = [9,8,5,1,3]
output = [1,3,5,8,9]
data = mergesort(data,0,len(data))
print(data)

subplot(1,2,1)
plt.plot(size,insert_time)
plt.xlabel("Size of List")
plt.ylabel("Time to sort")
plt.title("Insertion Sort")

merge()
subplot(1,2,2)
plt.plot(size,merge_sort_time)
plt.title("Merge Sort")
plt.xlabel("Size of List")
plt.ylabel("Time to sort")

plt.show()

