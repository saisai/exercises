
var groupAnagrams = function(strs){

	let obj = {};
	for(let str of strs){
		let letters = str.split("").sort().join("");
		obj[letters] ? obj[letters].push(str) : obj[letters] = [str];
	}

	return Object.values(obj);
}


var groupAnagrams2 = function(strs) {
	let m = new Map();
	for(let str of strs) {
		let sorted = str.split("").sort().join("");
		if(m.has(sorted)) m.set(sorted, [...m.get(sorted), str]);
		else m.set(sorted, [str]);
	}
	return Array.from(m.values());
}
var strs = ["eat","tea","tan","ate","nat","bat"];

console.log(groupAnagrams(strs));
console.log(groupAnagrams2(strs));

