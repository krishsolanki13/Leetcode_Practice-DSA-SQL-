# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if t == "":
#             return ""
        
#         countT = {}
#         for c in t:
#             countT[c] = 1 + countT.get(c,0)
        
#         res = [-1,-1]
#         reslen = float("infinity")

#         for i in range(len(s)):
#             countS = {}
#             for j in range(i,len(s)):
#                 countS[s[j]] = 1 + countS.get(s[j],0)

#                 flag = True
#                 for c in countT:
#                     if countT[c]>countS.get(c,0):
#                         flag = False
#                         break
                
#                 if flag and (j-i+1)<reslen:
#                     reslen = (j-i+1)
#                     res = [i,j]
        
#         l,r = res
#         return s[l:r+1] if reslen!=float("infinity") else ""



class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        res, reslen = [-1, -1], float("infinity")

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if (r-l+1) < reslen:
                    reslen = r-l+1
                    res = [l,r]
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have-=1
                
                l+=1
            
        l,r = res
    
        return s[l:r+1] if reslen != float("infinity") else ""
    
                

        
