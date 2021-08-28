let numbers = [1, 2, 3, 4, 5, 6]

function isOddNumber(number) {
	return number % 2	
}

const oddNumbers = numbers.filter(isOddNumber);
console.log(oddNumbers);

let oddNumbers2 = numbers.filter(function(number) {
    return number % 2;
});
console.log(oddNumbers2); // [ 1, 7, 3, 5 ]

let oddNumbers3 = numbers.filter(number => number % 2);
console.log(oddNumbers3);