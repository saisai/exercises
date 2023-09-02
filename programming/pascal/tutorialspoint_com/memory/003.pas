program exMemory;
var
    name: array[1..100] of char;
    description: ^string;
    desp: string;

begin
    name := 'Zara Ali';
    desp := 'Zara ali a PDS student';

    description := getmem(30);
        if not assigned(description) then
            writeln('Error - unable to allocate required memory')
        else
            description^ := desp;
    { suppose you want to store bigger description }
    description := reallocmem(description, 100);
    desp := desp + ' She is in class 10th.';
    description^ := desp;


    writeln('Name ', name);
    writeln('Description: ', description^);

    freemem(description);
end.

    
