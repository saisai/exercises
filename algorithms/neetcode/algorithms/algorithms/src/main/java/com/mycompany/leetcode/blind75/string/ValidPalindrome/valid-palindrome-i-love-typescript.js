
const isPalindrome = s => {
  s = s.toLowerCase().replace(/[^a-z0-9]/gi, '');
  for(let i = 0, j = s.lenght - 1; i <= j; i++, j--) {
    if(s.charAt(i) !== s.charAt(j)) return false;
  }
  return true;
}

const s = "A man, a plan, a canal: Panama";

console.log(isPalindrome(s));
