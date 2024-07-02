


def bubble_sort(arr):
    sorted=False
    while not sorted:
        sorted=True
        for i in range(1,len(arr)):
            if arr[i]<arr[i-1]:
                sorted=False
                arr[i],arr[i-1] = arr[i-1],arr[i]

if __name__ == "__main__":
    arr=list(range(1,23,2))
    print(arr)
    bubble_sort(arr)
    print(arr)