program exEnumeration;
type
  beverage = (coffee, tea, milk, water, coke, limejuice);

var
  drink: beverage;

begin
  writeln('Which drink do you want?');
  drink := limejuice;

  writeln('You can drink ', drink);
end.

