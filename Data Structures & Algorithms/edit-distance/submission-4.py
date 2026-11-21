
from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache 
        def dp(i,j):
            if i==0 or j==0 :
                return i or j
            if word1[i-1]==word2[j-1]:
                return dp(i-1,j-1)
            return 1+min(dp(i-1,j),dp(i,j-1),dp(i-1,j-1))
        return dp(len(word1),len(word2))
            
       
   
        