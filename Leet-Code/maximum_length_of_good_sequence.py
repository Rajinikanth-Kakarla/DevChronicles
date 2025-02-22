class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # Initialize the dp array where dp[i][j] represents the maximum length of a good subsequence
        # ending at index i with exactly j changes.
        dp = [[0] * (k + 1) for _ in range(n)]

        # Initialize dp[i][0] to 1 for all i since a single element is always a valid subsequence with 0 changes
        for i in range(n):
            dp[i][0] = 1

        # Fill the DP table
        for i in range(1, n):
            for j in range(i):
                for changes in range(k + 1):
                    if nums[i] == nums[j]:
                        dp[i][changes] = max(dp[i][changes], dp[j][changes] + 1)
                    elif changes > 0:
                        dp[i][changes] = max(dp[i][changes], dp[j][changes - 1] + 1)

        # Get the maximum value from the dp array considering up to k changes
        max_length = 0
        for i in range(n):
            for changes in range(k + 1):
                max_length = max(max_length, dp[i][changes])

        return max_length