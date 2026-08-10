class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Variation of "prefix sum" except in reverse and computing maximum
        n = len(arr)
        result = [-1] * n # prebuild array for efficient insertion
        for i in range(n - 2, -1, -1): # traverse backwards starting second to last
            # the item to the right in `result` stores then maximum of everything
            # previously examined while the item to the right in `arr` is the new
            # we are examining, so it's the max of either of these
            result[i] = max(result[i + 1], arr[i + 1]) 

        return result