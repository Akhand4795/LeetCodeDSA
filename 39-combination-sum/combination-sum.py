class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, current_sum, path):
            # Base case: if current_sum equals target, we found a valid combination
            if current_sum == target:
                result.append(path[:])
                return
            # If current_sum exceeds target, no need to continue
            if current_sum > target:
                return
            # Iterate through the candidates starting from the current index
            for i in range(start, len(candidates)):
                # Include the candidate in the current path
                path.append(candidates[i])
                # Recurse with updated current_sum and the same start index (allowing repeated elements)
                backtrack(i, current_sum + candidates[i], path)
                # Backtrack by removing the last added element
                path.pop()

        candidates.sort()  # Sorting the candidates
        result = []
        backtrack(0, 0, [])
        return result