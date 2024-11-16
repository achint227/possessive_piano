from random import shuffle

def quicksort_helper(arr, l, r):

    if l >= r:
        return

    pivot = arr[(l + r) // 2]

    index = partition(arr, l, r, pivot)

    quicksort_helper(arr, l, index - 1)
    quicksort_helper(arr, index, r)    





def partition(arr, l, r, pivot):

    while l <= r:

        while l <= r and arr[l] < pivot:
            l += 1
        
        while l <= r  and arr[r] > pivot:
            r -= 1
        
        arr[l], arr[r] = arr[r], arr[l]
        l, r = l + 1, r - 1
    
    return l

def quicksort(arr):

    quicksort_helper(arr, 0, len(arr) - 1)


l = list(range(2,33))

shuffle(l)

print(l)

quicksort(l)

print(l)