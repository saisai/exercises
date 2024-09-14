Program Lesson7_Program1;
Uses Crt;

Procedure DrawLine;
{ This procedure helps me to avoid the rewriting the for loops }
Var Counter : Integer;

Begin
    textcolor(green);
    For Counter := 1 to 10 do 
    Begin
        Write(chr(196));
    End;
End;

Begin
    GotoXy(10, 5);
    DrawLine;
    GotoXy(10,6);
	DrawLine;
	GotoXy(10,7);
	DrawLine;
	GotoXy(10,10);
	DrawLine;
	Readkey;
End.
