class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        ways = 0 
        def dfs(i):
            nonlocal ways
            if i == len(s):
                return 1                    # used every digit: one valid decoding
            if s[i] == "0":
                return 0                    # nothing can start with 0
            if i in cache:
                return cache[i]

            ways += dfs(i + 1)               # take 1 digit
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                ways += dfs(i + 2)          # take 2 digits

            cache[i] = ways
            return ways
        return dfs(0)