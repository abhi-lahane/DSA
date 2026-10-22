
def count_even_odd(arr):
    even = 0
    odd = 0

    for num in arr:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    print("Even =", even)
    print("Odd =", odd)


arr = [1, 2, 3, 4, 5, 6]
count_even_odd(arr)

# Even = 3
# Odd = 3