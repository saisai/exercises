Program Program3b_lesson4;
Uses Crt;
           
Var 
	Counter : Integer;  { will be used as a loop counter }
           
Begin

	For Counter := 1 to 5 do 
	Begin      
		gotoxy(25, 5 + Counter);
		Writeln('I');
	End;

	For Counter := 5 Downto 1 do
	Begin  {an example of 'downto' instead of 'to', note the 'gotoxy(_,_)'}
		gotoxy(32, 11 - Counter);
		Writeln('I');
	End;

	For Counter := 1 to 6 do
	Begin
		gotoxy(25 + Counter, 11);
		Writeln('-');
	End;

	For Counter := 6 Downto 1 do
	Begin
		gotoxy(32 - Counter, 5);
		Writeln('-');
	End;

	{--------------The Corners(+)---------------}
	Gotoxy(25,5);
	Writeln('+');
	GotoXy(25,11);
	Writeln('+');
	GotoXy(32,5);
	Writeln('+');
	GotoXy(32,11);
	Writeln('+');
	GotoXy(45,7); 
	Write('Made with For Loops :)');
	Readln;
End.
