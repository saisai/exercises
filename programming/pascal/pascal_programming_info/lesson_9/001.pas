
Type
  nameType = string[50];
  ageType = 0..150; { age range: from 0 to 150 }

var
  name : nameType;
  age : ageType;

begin
  write('Enter your name: ');
  Readln(name);
  write('Enter your age: ');
  Readln(age);
  writeln;
  writeln('You name: ', name);
  writeln('your age: ', age);
  readln;
end.
