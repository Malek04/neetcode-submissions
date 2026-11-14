class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        calc_map = {}
        l = []
        for i in nums:
            if i not in calc_map:
                calc_map[i] = nums.count(i)
        sorted_map = sorted(calc_map.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            l.append(sorted_map[i][0])
        return l