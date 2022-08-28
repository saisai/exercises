/*

https://cplusplus.com/reference/vector/vector/vector/

https://leetcode.com/problems/largest-sum-of-averages/discuss/126003/C%2B%2B-DP-Simple-Solution-use-O(N*K)-Space-and-O(K*N2)-Time-With-Detailed-Explanation
https://leetcode.com/problems/largest-sum-of-averages/
*/



#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    double largestSumOfAverages(vector<int>& A, int K) {
        int n = A.size();
        vector<int> sum(n + 1, 0);
        for(int i = 0; i < n; ++i){
        	sum[i + 1] = sum[i] + A[i];
        }
        if(K <= 1){
        	return (1.0 * sum[n]) / n;
        }
        if(K >= n){
        	return sum[n];
        }
        vector<vector<double>> dp(n + 1, vector<double>(K + 1, 0.0));
        for(int i = 1; i <= n; ++i){
        	dp[i][1] = (1.0 * sum[i]) / i;
        }
        for(int k = 2; k <= K; ++k){
        	for(int i = k; i <= n; ++i){
        		for(int j = i - 1; j >= k - 1; --j){
        			dp[i][k] = max(dp[i][k], dp[j][k - 1] + 1.0 * (sum[i] - sum[j]) / (i - j));
        		}
        		
        	}
        }
        return dp[n][K];
    }
};

int main () {
  Solution s;
  
  int myints[] = {9,1,2,3,9};
  std::vector<int> nums (myints, myints + sizeof(myints) / sizeof(int) );  
  int k = 3;
  double result = s.largestSumOfAverages (nums, k);
  cout << "area: " << result;
  return 0;
}