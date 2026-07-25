class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l=[[] for _ in range(len(nums)+1)]
        count=Counter(nums)
        for item,cnt in count.items():
            l[cnt].append(item)
        
        res=[]
        for cnt in range(len(nums),0,-1):
            for item in l[cnt]:
                res.append(item)
                if len(res)==k:
                    return res
