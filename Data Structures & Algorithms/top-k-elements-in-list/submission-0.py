from collections import Counter
from functools import reduce

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        
        return list(
            map(
                lambda pair: pair[0],                               # 3. 映射提取出数字
                sorted(freq_map.items(), key=lambda x: x[1], reverse=True)[:k]  # 2. 按频率降序排序并截取前 k 个
            )
        )