def max_consecutive_ones(arr):
    count = 0
    maximum = 0

    for num in arr:
        if num == 1:
            count += 1
            maximum = max(maximum, count)
        else:
            count = 0

    return maximum


arr = [1, 1, 0, 1, 1, 1]
print(max_consecutive_ones(arr))

# o/p = 3