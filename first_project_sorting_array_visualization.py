import matplotlib.pyplot as plt
import numpy as np
import time


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                update_plot(arr)
               
                time.sleep(0.1)
   

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        update_plot(arr)
        time.sleep(0.1)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        update_plot(arr)
        time.sleep(0.1)

def update_plot(arr):
    plt.clf()
    plt.bar(range(len(arr)), arr)
    plt.show()
    plt.pause(0.00000001)

def main():
    #np.random.seed(0)  # For reproducibility
 #   array = np.random.randint(1, 100, 15)
    array=[2,4,5,90,79,3,9,11,12,54,45,76,12,34]

    plt.ion()  

    print("Original Array:", array)
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(array)), array)
    plt.title("Original Array")
    plt.show()

    bubble_sorted_array = array.copy()
    bubble_sort(bubble_sorted_array)

    selection_sorted_array = array.copy()
    selection_sort(selection_sorted_array)

    merge_sorted_array = array.copy()
    merge_sort(merge_sorted_array)

    plt.ioff() 
    plt.show()

if __name__ == "__main__":
    main()
