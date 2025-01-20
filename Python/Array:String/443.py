class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        string = ""
        idx = 0
        if len(chars) == 1:
            return len(chars)
        while idx < len(chars) - 1:
            repeat = 1
            while idx < len(chars) - 1 and chars[idx] == chars[idx + 1]:
                repeat += 1
                del chars[idx + 1]
            if repeat == 1:
                idx += 1
            else:
                string = str(repeat)
                chars[idx + 1:idx + 1] = list(string)
                idx += len(string) + 1
        return len(chars)


Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
