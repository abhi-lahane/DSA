def missing_number(arr, n):
    total = n * (n + 1) // 2
    arr_sum = 0

    for num in arr:
        arr_sum += num

    return total - arr_sum


arr = [1, 2, 4, 5]
n = 5

print(missing_number(arr, n))
