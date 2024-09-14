let employees = [
    {name: 'John', salary: 90000, hireDate: "July 1, 2010"},
    {name: 'David', salary: 75000, hireDate: "August 15, 2009"},
    {name: 'Ana', salary: 80000, hireDate: "December 12, 2011"}
];

// sort by salary
employees.sort(function(x, y) {
	return x.salary - y.salary;
});

console.table(employees);

employees.sort(function(x, y){
  let a = x.name.toUpperCase(),
      b = y.name.toUpperCase();
  return a == b ? 0 : a > b ? 1 : -1;
});

console.table(employees)

employees.sort(function(x, y) {
  let a = new Date(x.hireDate),
      b = new Date(y.hireDate);
  return a - b;
});
console.table(employees);

