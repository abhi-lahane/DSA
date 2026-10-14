
n = int(input("Enter a number: "))

total = 0

while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10

print("Sum of digits =", total)

#o/p = Enter a number: 1234
#      Sum of digits = 10