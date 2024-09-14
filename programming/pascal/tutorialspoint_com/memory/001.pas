program exMemory;
var
    name: array[1..100] of char;
    description: ^string;

begin
    name := 'Zara Ali';

    new(description);
        if not assigned(description) then
            writeln('Error - unable to allocate required memory')
        else
            description^ := 'Zara ali a DPS student in class 10th';
    writeln('Name = ', name);
    writeln('Description: ', description^);
end.

