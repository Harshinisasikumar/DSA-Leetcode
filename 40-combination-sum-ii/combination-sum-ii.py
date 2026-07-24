from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def backtrack(start, path, total):
            if total == target:
                ans.append(path[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since array is sorted, no need to continue
                if total + candidates[i] > target:
                    break

                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])  # Use each number only once
                path.pop()

        backtrack(0, [], 0)
        return ans