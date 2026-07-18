class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max=0
        for i in range(len(heights)):
            area=0
            b=0
            for j in range(len(heights)):
                if i==j:
                    continue
                else:
                    b=abs(j-i)
                    l1=heights[i]
                    l2=heights[j]
                    area=min(l1,l2)*b
                    if area > max:
                        max = area 
        return max
