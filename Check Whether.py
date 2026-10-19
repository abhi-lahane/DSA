
def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False

    return True


arr = [1, 2, 3, 4, 5]
print(is_sorted(arr))


# [1, 2, 3, 4, 5]  → True
# [1, 3, 2, 4, 5]  → False
# [2, 2, 3, 4]     → True
#o/p = True