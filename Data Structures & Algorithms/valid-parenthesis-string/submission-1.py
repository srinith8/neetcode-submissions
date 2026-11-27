class Solution:
    def checkValidString(self, s: str) -> bool:
        left=[]
        star=[]
        for i,ch in enumerate(s):
            if ch=='(':
                left.append(i)
            elif ch=='*':
                star.append(i)
            else:
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while len(left) and len(star):
            if left[-1]<star[-1]:
                left.pop()
                star.pop()
            else:
                return False
        return len(left)==0



        