from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # cnt[d] = number of elements divisible by d
        cnt = [0] * (mx + 1)
        for d in range(1, mx + 1):
            for m in range(d, mx + 1, d):
                cnt[d] += freq[m]

        # exact[d] = number of pairs whose gcd is exactly d
        exact = [0] * (mx + 1)
        for d in range(mx, 0, -1):
            c = cnt[d]
            pairs = c * (c - 1) // 2
            m = 2 * d
            while m <= mx:
                pairs -= exact[m]
                m += d
            exact[d] = pairs

        prefix = []
        values = []
        total = 0
        for d in range(1, mx + 1):
            if exact[d]:
                total += exact[d]
                prefix.append(total)
                values.append(d)

        ans = []
        for q in queries:
            idx = bisect_right(prefix, q)
            ans.append(values[idx])

        return ans