
const change = function(amount, coins) {
	const dp = new Array(amount + 1).fill(0);
	dp[0] = 1;

	for (let i = 0,  { length } = coins; i < length; i+=1) {
		for(let j = coins[i]; j <= amount; j += 1) {
			dp[j] += dp[j - coins[i]];
		}
	}
	return dp[amount];

};
let amount = 5, coins = [1,2,5]
console.log(change(amount, coins))

