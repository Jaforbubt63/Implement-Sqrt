class Solution:
    def mySqrt(self, x: int) -> int:
        
        low, high = 0, x
        
        while low <= high:
            mid = (low + high) // 2
            if(mid * mid) <= x and ((mid+1)*(mid-1)):
                break
            if mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
                
        return mid
                
        