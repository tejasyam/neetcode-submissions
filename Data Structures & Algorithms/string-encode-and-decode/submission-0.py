class Solution:


    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            n = len(i)
            s += str(n)
            s = s + "#" + i
        return s



    def decode(self, s: str) -> List[str]:
        l = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            n = int(s[i:j])
            s1 = s[j+1:j+1+n]
            l.append(s1)

            i = j + 1 + n

        return l