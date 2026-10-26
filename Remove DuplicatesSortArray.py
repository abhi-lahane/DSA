def remove_duplicates(arr):
    if len(arr) == 0:
        return []

    j = 0

    for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]

    return arr[:j + 1]


arr = [1, 1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(arr))