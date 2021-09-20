program DNA_Base_Count;
{$IFDEF FPC}
    {$MODE DELPHI}//String = AnsiString
{$ELSE}
    {$APPTYPE CONSOLE}
{$ENDIF}
const
    dna = 
    'CGTAAAAAATTACAACGTCCTTTGGCTATCTCTTAAACTCCTGCTAAATG' +
        'CTCGTGCTTTCCAATTATGTAAGCGTTCCGAGACGGGGTGGTCGATTCTG' +
        'AGGACAAAGGTCAAGATGGAGCGCATCGAACGCAATAAGGATCATTTGAT' +
        'GGGACGTTTCGTCGACAAAGTCTTGTTTCGAGAGTAACGGCTACCGTCTT' +
        'CGATTCTGCTTATAACACTATGTTCTTATGAAATGGATGTTCTGAGTTGG' +
        'TCAGTCCCAATGTGCGGGGTTTCTTTTAGTACGTCGGGAGTGGTATTATA' +
        'TTTAATTTTTCTATATAGCGATCTGTATTTAAGCAATTCATTTAGGTTAT' +
        'CGCCGCGATGCTCGGTTCGGACCGCCAAGCATCTGGCTCCACTGCTAGTG' +
        'TCCTAAATTTGAATGGCAAACACAAATAAGATTTAGCAATTCGTGTAGAC' +
        'GACCGGGGACTTGCATGATGGGAGCAGCTTTGTTAAACTACGAACGTAAT';

var
    CntIdx : array of NativeUint;
    DNABases : string;
    SumBaseTotal : NativeInt;

procedure OutFormatBase(var DNA: string; colWidth: NativeInt);
var
    j: NativeInt;
begin
    j := 0;
    writeln(' DNA base sequence');
    while j < length(DNA) do
        begin
            writeln(j:5, copy(DNA, j+1, colWidth): colWidth+2);
            inc(j, colWidth);
        end;
        writeln;
end;

procedure Cnt(const DNA: string);
var
    i,p :NativeInt;
begin
    setlength(CntIdx, length(DNABases));
    i := 1;
    while i <= length(DNA) do
    begin
        p := pos(DNA[i], DNABases);
        // found new base so extend list
        if p = 0 then
        begin
            DNABases := DNABases+DNA[i];
            p := length(DNABases);
            setlength(CntIdx, p+1);
        end;
        inc(CntIdx[p]);
        inc(i);
    end;

    writeln('Base  Count');
    SumBaseTotal := 0;
    for i := 1 to length(DNABases) do
    begin
        p := CntIdx[i];
        inc(SumBaseTotal, p);
        writeln(DNABases[i]:4, p:10);
    end;
    writeln('Total base count ', SumBaseTotal);
    writeln;
end;

var
    TestDNA: string;
begin
    DNABases := 'ACGT'; // predefined
    TestDNA := DNA;
    OutFormatBase(TestDNA, 50);
    Cnt(TestDNA);
end.



