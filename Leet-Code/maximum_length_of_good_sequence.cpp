class Solution {
public:
    std::map<int, int> f[55];
    int n, k, g[55], a[5005];
    int maximumLength(vector<int>& nums, int k_) {
        n = nums.size();
        k = k_;
        for(int i = 1; i <= n; ++i) a[i] = nums[i - 1];
        for(int i = 1; i <= n; ++i){
            for(int s = 0; s <= k; ++s){
                f[s][a[i]] = f[s][a[i]] + 1;
                if(s > 0) f[s][a[i]] = std::max(f[s][a[i]], g[s - 1] + 1);
            }
            for(int s = 0; s <= k; ++s) g[s] = std::max(g[s], f[s][a[i]]);
        }
        int ans = 0;
        for(int i = 0; i <= k; ++i) ans = std::max(ans, g[i]);
        return ans;
    }
};