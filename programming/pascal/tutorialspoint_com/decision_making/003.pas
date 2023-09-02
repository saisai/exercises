program ifelse_ifelseChecking;
var
  a : integer;

begin
  a := 100;
  if(a = 10) then
    writeln('value of a is 10')
  else if(a = 20) then
    writeln('value of a is 20')
  else if(a = 30) then
    writeln('value of a is 30')
  else
    writeln('None of the values is matching');
    writeln('Exact value of a is :', a);
  end.

