class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set1=set()
        for i,x in enumerate(nums):
            set1.add(x)
            if len(set1)-1 != i:
                return True

        return False