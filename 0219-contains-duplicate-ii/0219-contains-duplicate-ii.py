class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        windows = set()
        left = 0
        
        
        for right in range(len(nums)):
            if (right - left) > k:
                windows.remove(nums[left])
                left+=1
            if nums[right] in windows:
                return True
            windows.add(nums[right])
        return False
            