class Solution:
	def count(self,arr, n, x):
        count=0
        for i in arr:
            if i==x:
                count=count+1
        return count
