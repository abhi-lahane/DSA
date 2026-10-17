
def find_smallest(arr):
    smallest = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]

    return smallest


arr = [12, 5, 30, 2, 18]
print(find_smallest(arr))
