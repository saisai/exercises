var
	s : string;

begin
	s := 'hey there! How are you?';
	write('The word "how" is found at char index ');
	writeln(pos('how', s));
	if pos('Why', s) <= 0 then
		writeln('"Why" is not found.');
end.
