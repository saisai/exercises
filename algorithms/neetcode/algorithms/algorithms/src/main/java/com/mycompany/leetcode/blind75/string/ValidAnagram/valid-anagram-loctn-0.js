

var isAnagram = function(s, t){
	if(t.length !== s.length) return false;
	const counts = {};
	for(let c of s) {
		counts[c] = (counts[c] || 0 ) + 1;
	}

	for(let c of t) {
		if(!counts[c]) return false;
		counts[c]--;
	}

	return true;	
}

var isAnagram2 = function(s, t, m = {}) {
	for(let c of s) m[c] = (m[c] || 0) + 1;
	for(let c of t) if(!m[c]--) return false;
	return Object.values(m).every(v => !v);
}

var s = "anagram", t = "nagaram";
console.log(isAnagram(s, t));
console.log(isAnagram2(s, t));



