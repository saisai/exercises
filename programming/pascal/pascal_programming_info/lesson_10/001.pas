var 
	myString : String;

begin
	myString := 'Hey! How are you?';
	writeln('The length of the string is ', byte(myString[0]));
	writeln(myString[byte(myString[0])]);
	write(' is teh last charachter.');
end.
