Uses Crt;
Var YN: String;

Begin
    Writeln('Y(YES) or N(NO)?');
    Repeat {repeat the code for at least one time }
        YN := ReadKey;
        If YN = 'y' Then Halt; { Halt - exit }
        IF YN = 'n' Then Writeln('why not? Exiting...');
        Delay(1800); { Wait a second plus 800 milliseconds }
    Until (YN = 'y') OR (YN = 'n');
End.
