var
	s : string;
	i : integer;

begin
	s := 'Hey! How are you?';
	for i := 1 to length(s) do
		s[i] := upcase(s[i]);
	write(s); { 'hey how are you?' }
end.

