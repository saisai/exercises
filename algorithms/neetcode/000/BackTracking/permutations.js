
var permute = function(nums, set=[], answers=[]) {
	if (!nums.length) answers.push([...set]);

	for(let i=0; i < nums.length; i++){
		const newNums = nums.filter((n, index) => index != i);
		set.push(nums[i]);
		permute(newNums, set, answers);
		set.pop();
	}
	return answers;
};

console.log(permute([1,2,3]))

const results = permute(['b1','b2','g'])

results.forEach(function(result){
	if(JSON.stringify(['b1','g','b2']) !== JSON.stringify(result) &&
		JSON.stringify(['b2','g','b1']) !== JSON.stringify(result))
	{
	console.log(result)
	}
});
