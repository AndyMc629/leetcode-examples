
# Attempted mathsy solution
# import math
# from typing import List
# class Solution:
#     def isPalindrome(self, x: int) -> List[int]:
#         n = 0
#         processing = True
#         values = []
#         while processing is True:
#             value_calc = math.floor((x*math.pow(10, -n))%10)
#             print(value_calc)
#             if math.isclose(0, value_calc) is True:
#                 processing = False
#             else:
#                 values.append(value_calc)
#                 n += 1

#         return values

# Simple string based solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        if x_str[::-1] == x_str:
            return True
        else:
            return False

# Without string, only need to halferse first half and compare to second half ...
# my first attempt was definitely getting close, key thing here is that 0 or anything divisible by 10
# are obv not palindromes and the piece about lookng halfwise.
class Solution:
    def isPalindrome(x: int) -> bool:
        if x < 0 or (x != 0 and x%10 == 0):
            return False
        half = 0
        while x > half:
            half = half*10 + x%10
            x = x//10
        # second case accounts for when there is an odd number of digits -> the half then has an extra digit at this point.
        return x == half or x == half//10


if __name__=="__main__":
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(-121))
    print(s.isPalindrome(10))
    print(s.isPalindrome(-101))
    print(s.isPalindrome(34043))