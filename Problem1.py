# TC and SC - O(2^n) and O(n)
class Solution:
    def subsets(self, nums):
        res = []
        subset = []     
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return            
            #We choose i
            subset.append(nums[i])
            dfs(i+1)
            
            #we dont choose i
            subset.pop()
            dfs(i+1)
            
        dfs(0)
        return res    