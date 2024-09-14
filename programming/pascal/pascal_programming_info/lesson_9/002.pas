uses Crt;
Type
	myRange = 1..5;
	arrayIntType = Array[myRange] of Integer;
	myFileType = File of arrayIntType;

var 
	i : myRange;
	myFile : myFileType; {  the next array is 2 dimensional }
	arrayInt : Array[1..2] of arrayIntType;

begin
	clrscr;
	randomize;

	for i := i to 5 do { or we can use length(arrayInt[1][i]) }
	begin
		arrayInt[1][i] := Random(1000);
		writeln('rand num: ', arrayInt[1][i]);
	end;

	assign(myFile, 'test.dat');
	rewrite(myFile);
	write(myFile, arrayInt[1]);
	close(myFile);
	reset(myFile);
	read(myFile, arrayInt[2]);
	close(myFile);

	for i := 1 to 5 do 
		writeln(i, ': ', arrayInt[2][i]);

	readln;

end.
