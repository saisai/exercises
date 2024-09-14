Program Lesson7_Program1a;
Uses Crt;
Var Counter : Integer;

Begin
	textcolor(green);

	GotoXy(10,5);
	For Counter := 1 to 10 do
	Begin 
		Write(chr(196));
	End;

	GotoXy(10,6);
	For Counter := 1 to 10 do
	Begin 
		Write(chr(196)); 
	End;

	GotoXy(10,7);
	For Counter := 1 to 10 do
	Begin 
		Write(chr(196)); 
	End; 

	GotoXy(10,10);
	For Counter := 1 to 10 do
	Begin 
		Write(chr(196)); 
	End; 

	Readkey;
End.
