program exPointers;

var
  number: integer;
  iptr: ^integer;
  y: ^word;

begin
  iptr := nil;
  y := addr(iptr);

  writeln('the value of iptr is ', y^);

end.

