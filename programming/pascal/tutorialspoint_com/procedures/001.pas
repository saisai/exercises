program exProcedure;
var
  a, b, c, min : integer;

procedure findMin(x, y, z: integer; var m: integer);
(* finds the minimum of the 3 values *)

begin
  if x < y then
    m := x
  else
    m := y;
  
  if z < m then
    m := z;
end; { end of procedure findMin }

begin
  writeln(' Enter three members: ');
  readln(a, b, c);
  findMin(a, b, c, min); (* Procedure call *)

  writeln(' Minimun: ', min);
end.

