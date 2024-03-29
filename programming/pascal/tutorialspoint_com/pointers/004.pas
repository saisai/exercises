program exPointers;

const 
  MAX = 3;

var 
  arr: array [1..MAX] of integer = (10, 100, 200);
  i: integer;
  iptr: ^integer;
  y: ^word;

begin
  (* let us have array address in pointer *)
  iptr := @arr[1];

  for i := 1 to MAX do
    begin
      y := addr(iptr);
      writeln('Address of arr [', i , '] = ', y^);
      writeln(' Value of arr[', i, '] = ', iptr^);

      { move to the next location }
      inc(iptr);
    end;
end.

