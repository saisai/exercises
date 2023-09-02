program exPointers;
const
  MAX = 3;

var
  arr: array [1..MAX] of integer = (10, 100, 200);
  i: integer;
  iptr: ^integer;
  y: ^word;

begin
  i := 1;

  (* let us have array address in pointer *)
  iptr := @arr[1];

  while (iptr <= @arr[MAX]) do
    begin
      y := addr(iptr);
      writeln('Adderss of arr[', i, ']= ', y^);
      writeln(' Value of arr[', i, '] = ', iptr^);

      { move to the next location }
      inc(iptr);
      i := i+1;
    end;
end.

