class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_value_map = {
            'I': 1,       
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        i = 0
        while i<len(s):
            if i==len(s)-1:
                total += symbol_value_map[s[i]]
                break
            elif symbol_value_map[s[i+1]]>symbol_value_map[s[i]]:
                total += (symbol_value_map[s[i+1]]-symbol_value_map[s[i]])
                i += 2
            else:
                total += symbol_value_map[s[i]]
                i += 1
        return total


if __name__=="__main__":
    s = Solution()
    print(s.romanToInt("III"))
    print(s.romanToInt("IV"))
    print(s.romanToInt("IX"))
    print(s.romanToInt("LVIII"))
    print(s.romanToInt("MCMXCIV"))