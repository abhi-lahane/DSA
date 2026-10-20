class solution:
    def smallnumbersthancurrent(self, nums: list[int]) ->list[int]:
        ans =[]
        for i in nums:
            c=0
            for j in nums:
                if j<i:
                    c+=1
            ans.append(c)
        return ans 
nums=[8,1,2,2,3]
obj = solution()
print(obj.smallnumbersthancurrent(nums))
