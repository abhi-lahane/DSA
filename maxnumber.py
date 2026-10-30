def findMax(arr):
    maximum = arr[0]

    for i in range(len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]

    return maximum