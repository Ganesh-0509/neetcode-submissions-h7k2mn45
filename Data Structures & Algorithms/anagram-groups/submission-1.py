class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for i in strs:
            x="".join(sorted(i))
            group[x].append(i)
        return list(group.values())
        