class solution:
    def FizzBuzz(self, n: int)-> list[str]:
        ans = []
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                ans.append("Fizzbuzz")
            elif i%3==0:
                ans.append("Fizz")
            elif i%5==0:
                ans.append("Buzz")
            else:
                ans.append(str(i))

        return ans
n=int(input("ENter the number"))
obj =solution()
print(obj.FizzBuzz(n))
