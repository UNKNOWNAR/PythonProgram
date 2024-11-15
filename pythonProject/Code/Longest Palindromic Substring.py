class Solution(object):
    def longestPalindrome(self, s):
        maps={}
        rs = ""
        c=''
        if len(s)==1:
            return s
        for idx,char in enumerate(s):
            if char in maps:
                if maps[c]-maps[char]==idx-maps[c]:
                    str = s[maps[char]:idx+1]
                    rs = str if len(str) > len(rs) else rs
                elif (maps[c] == idx-1):
                    if (c == char):
                        str = s[maps[char]:idx + 1]
                        rs = str if len(str) > len(rs) else rs
                        idx = maps[char]
                else:
                    c = char
                    del maps[char]
            else:
                c = char
            maps[char] = idx
        if(len(rs)==0):
            rs = s[0]
        return rs
if __name__=="__main__":
        obj = Solution()
        print(obj.longestPalindrome("ccc"))