class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x=[]
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j]==target:
                    x.append(i+1)
                    x.append(j+1)
        return x
        