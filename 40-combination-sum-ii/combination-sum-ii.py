class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []

        def backtrack(start, remaining, current):
            if remaining == 0:
                result.append(current[:])
                return

            if remaining < 0:
                return

            for i in range(start, len(candidates)):

                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since array is sorted
                if candidates[i] > remaining:
                    break

                current.append(candidates[i])

                # i + 1 means we cannot reuse the same element
                backtrack(i + 1, remaining - candidates[i], current)

                # Backtrack
                current.pop()

        backtrack(0, target, [])

        return result  