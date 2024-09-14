program exPointersFromFunctions;

type
  ptr = ^integer;

var
  i: integer;
  iptr: ptr;

function getValue(var num: integer): ptr;

begin
  getValue := @num;
end;

begin
  i := 100;
  iptr := getValue(i);

  writeln('Value deferenced: ', iptr^);

end.

