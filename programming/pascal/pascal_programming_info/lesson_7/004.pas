Program Lesson7_Program4;
Uses Crt;
Var SizeA, sizeB : Real;
	YN : Char;
	unitS : String[2];

Function PythagorasFunc(A: Real; B: Real) : Real; { The pythagoras theorem }
Begin
	PythagorasFunc := SQRT(A * A + B * B);
	{ Output: Assign the function name to the value.
	If you forget to assign the function to the value,
	you will get a trash value from memory }
End;

Begin

	Repeat
		Writeln;
		Write('Enter the size of side A : ');
		Readln(sizeA);
		Write('Enter the size of side B : ');
		Readln(sizeB);

		Repeat
			Write('metres or centimetres? Enter : [m or cm] ');
			Readln(unitS);
		Until (unitS = 'm') OR (unitS = 'cm');

		Writeln(PythagorasFunc(sizeA,sizeB),' ',unitS);
		Writeln;
		Write('Repeat? ');
		YN := Readkey;
	Until (YN IN ['N','n']);

End.
