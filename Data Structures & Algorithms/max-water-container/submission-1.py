class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = m = area = 0
        r = len(heights) - 1
        while l < r:
            area = (r-l) * min(heights[l],heights[r])
            m = max(m,area)
            if min(heights[r],heights[l]) == heights[r]:
                r -= 1
            else:
                l += 1
        return m