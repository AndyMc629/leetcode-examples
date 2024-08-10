class Solution:
    def isValid(self, s: str) -> bool:
        bracks = {
            '(':')',
            '[':']',
            '{':'}'
        }
        
        if len(s)==1:
            return False
        if s[0] in bracks.values():
            return False

        mylist = []
        for element in s:
            # is this element an opening bracket? 
            # add to stack if previous item wasn't an opening bracket too.
            if element in bracks:
                mylist.append(element)
            elif element in bracks and (mylist[-1] in bracks):
                return False
            # or is this element a closing bracket?
            elif element in bracks.values():
                # is the opening bracket for this the last item added?
                # Then pop stack to clear it for next couple.
                if bracks[mylist[-1]] == element:
                    mylist.pop()
                # If brackets don't pair, we've proven false.
                else:
                    return False
        # If we got to here, all brackets have paired.
        return True
                
if __name__=="__main__":
    s = Solution()
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))
    print(s.isValid("["))