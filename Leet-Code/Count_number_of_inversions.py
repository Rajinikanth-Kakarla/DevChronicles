MOD = 10**9 + 7

class Solution(object):
    def numberOfPermutations(self, n, requirements):
        """
        :type n: int
        :type requirements: List[List[int]]
        :rtype: int
        """
        # Precompute the maximum required inversions
        max_inversions = max(cnt for _, cnt in requirements)
        
        # Initialize DP table for up to n elements and max_inversions inversions
        dp = [[0] * (max_inversions + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            prefix_sum = [0] * (max_inversions + 2)
            for k in range(max_inversions + 1):
                prefix_sum[k + 1] = (prefix_sum[k] + dp[i - 1][k]) % MOD
            for k in range(max_inversions + 1):
                if k >= i:
                    dp[i][k] = (prefix_sum[k + 1] - prefix_sum[k - i + 1] + MOD) % MOD
                else:
                    dp[i][k] = prefix_sum[k + 1] % MOD

        # Create a map from the requirements for quick lookup
        req_map = {endi: cnti for endi, cnti in requirements}

        # Initialize the final DP table for filtering results based on requirements
        final_dp = [[0] * (max_inversions + 1) for _ in range(n + 1)]
        final_dp[0][0] = 1

        for i in range(1, n + 1):
            for k in range(max_inversions + 1):
                if (i - 1) in req_map and req_map[i - 1] != k:
                    continue
                for j in range(min(k + 1, i)):
                    final_dp[i][k] = (final_dp[i][k] + final_dp[i - 1][k - j]) % MOD

        # Calculate the final answer
        answer = 0
        if (n - 1) in req_map:
            answer = final_dp[n][req_map[n - 1]]
        else:
            for k in range(max_inversions + 1):
                answer = (answer + final_dp[n][k]) % MOD

        return answer