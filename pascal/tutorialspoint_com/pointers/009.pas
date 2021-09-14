program exPointertoPointers;
type
  iptr = ^integer;
  pointerptr = ^iptr;

var
  num: integer;
  ptr: iptr;
  pptr: pointerptr;
  x, y: ^word;

begin
  num := 3000;

  (* take the addres of var *)
  ptr := @num;

  { take the address of ptr using address of operator @ }
  pptr := @ptr;

  { let us see the value and the address }
  x := addr(ptr);
  y := addr(pptr);

  writeln('Value of num = ', num);
  writeln('Value available at ptr^ = ', ptr^);
  writeln('Value availabe at pptr^^ = ', pptr^^);
  writeln('Addres at ptr = ', x^);
  writeln('Address at pptr = ', y^);

end.
