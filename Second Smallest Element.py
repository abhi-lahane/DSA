def second_smallest(arr):
    smallest = float('inf')
    second = float('inf')

    for num in arr:
        if num < smallest:
            second = smallest
            smallest = num
        elif num < second and num != smallest:
            second = num

    if second == float('inf'):
        return -1

    return second


arr = [8, 3, 5, 1, 6]
print(second_smallest(arr))