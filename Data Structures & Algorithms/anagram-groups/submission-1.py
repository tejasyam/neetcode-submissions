class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        used = [False] * len(strs)

        for i in range(len(strs)):
            if used[i] == True:
                continue

            sub = [strs[i]]
            used[i] = True

            for j in range(i + 1, len(strs)):
                if used[j] == False:
                    x = self.isAnagram(strs[i], strs[j])
                    if x == True:
                        sub.append(strs[j])
                        used[j] = True

            ans.append(sub)

        return ans
        

    def isAnagram(self, s: str, t: str) -> bool:
        s1="".join(sorted(s))
        t1="".join(sorted(t))
        count=0
        if (len(s1)==len(t1)):
            for i,j in zip(s1,t1):
                if i==j:
                    count+=1
                else:
                    pass
            if count==len(s1):
                return True
            else:
                return False
        else:
            return False
