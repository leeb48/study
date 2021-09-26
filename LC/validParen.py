class Solution:
    def isValid(self, s: str) -> bool:

        bracketDict = {
            '}': '{',
            ')': '(',
            ']': '['
        }

        stack = []

        for c in s:
            if c in dict.values():
                stack.append(c)
            else:
                if stack == [] or bracketDict[c] != stack.pop():
                    return False

        return True if len(stack) == 0 else False


test = ']'

mySolution = Solution()

print(mySolution.isValid(test))
