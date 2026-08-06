class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums) # n is lenght of the array
        window = 0 # window state is the number of 1s (so just sum)
        left = 0 # pointer to left side of window
        ans = 0

        for right in range(n): # pointer to right side of window 
            window += nums[right] # add the current rightmost to the window state
            
            # slide window while the window contains any zeros. This is when window
            # state is not equal to window size (right - left + 1)
            while right - left + 1 != window:
                window -= nums[left] # remove leftmost value from window
                left += 1 # move left pointer along by 1

            # answer is the highest value of the window state encountered
            ans = max(ans, window)
        
        return ans






        

