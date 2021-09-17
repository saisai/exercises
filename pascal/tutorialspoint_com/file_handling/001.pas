program DataFiles;
type
  StudentRecord = Record
  s_name: string;
  s_addr: string;
  s_batchcode: string;
  end;

var
  Student: StudentRecord;
  f: file of StudentRecord;

begin
  assign(f, 'students.dat');
  rewrite(f);
  Student.s_name := 'Jhon Smith';
  Student.s_addr := 'United States of America';
  Student.s_batchcode := 'Computer Science';
  write(f, Student);
  close(f);
end.

