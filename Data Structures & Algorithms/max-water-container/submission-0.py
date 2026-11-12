class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = m = area = 0
        r = 1
        while r < len(heights):
            area = (r-l) * min(heights[l],heights[r])
            m = max(m,area)
            if heights[r] > heights[l]:
                l = r
            r += 1

        return m