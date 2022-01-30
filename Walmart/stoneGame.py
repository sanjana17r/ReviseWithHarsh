def stoneGame(self, arr: List[int]) -> bool:
        n = len(arr)
        t = {}
        def dp(i, j):
            if i > j:
                return 0
            if (i, j) in t:
                return t[(i, j)]
            # player chooses last element
            ans = 0
            x = arr[j] + min(dp(i+1, j-1), dp(i, j-2)) # here we are taking min because we are
            # assuming the opponent makes optimal moves
            z = arr[i] + min(dp(i+2, j), dp(i+1, j-1))
            ans += max(x, z) # here we are taking max inorder to find max cost the first player
            # can obtain assuming opponent plays "smart"!
            t[(i, j)] = ans
            return t[(i, j)]
        return dp(0, n-1)>sum(arr)//2
