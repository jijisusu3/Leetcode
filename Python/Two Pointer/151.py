class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        return " ".join(s[::-1])
        # l = ""
        # r = ""
        # left = 0
        # right = len(s) - 1
        # while left < right:
        #     leftString = ""
        #     rightString = ""
        #     while left < right and s[left] != " ":
        #         leftString += s[left]
        #         left += 1
        #     while left < right and s[right] != " ":
        #         rightString = s[right] + rightString
        #         right -= 1
        #     left += 1
        #     right -= 1
        #
        #     if leftString != "":
        #         if l != "":
        #             l = leftString + " " + l
        #         else:
        #             l = leftString
        #     if rightString != "":
        #         if r != "":
        #             r = r + " " + rightString
        #         else:
        #             r = rightString
        # return r + " " + l

Solution().reverseWords("  the sky  is blue   ")

