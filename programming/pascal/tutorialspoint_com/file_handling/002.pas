program DataFiles;
type
  StudentRecord = Record
    s_name : string;
    s_addr: string;
    s_batchcode: string;
  end;

var 
  Student: StudentRecord;
  f: file of StudentRecord;

begin
  assign(f, 'students.dat');
  reset(f);
  while not eof(f) do
    begin
      read(f, Student);
      writeln('Name: ', Student.s_name);
      writeln('Address: ', Student.s_addr);
      writeln('Batch Code: ', Student.s_batchcode);
    end;

  close(f);
end.


