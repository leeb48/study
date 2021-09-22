class Solution:
    def romanToInt(self, s: str) -> int:

        numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        sum = 0
        for i in range(0, len(s)):
            sum += numerals[s[i]]

            if i > 0 and numerals[s[i]] > numerals[s[i - 1]]:
                sum -= numerals[s[i - 1]] * 2

        return sum


romanNumeral = "MCMXCIV"

solution = Solution()


print(solution.romanToInt(romanNumeral))
