
def find_largest(arr):
    largest = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]

    return largest


arr = [10, 25, 7, 40, 15]
print(find_largest(arr))
