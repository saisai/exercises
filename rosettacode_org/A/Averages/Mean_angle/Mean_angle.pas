program MeanAngle;
{$IFDEF DELPHI}
  {$APPTYPE CONSOLE}
{$ENDIF}
uses
  math; // sincos and atan2
type
  tAngles = array of double;
function MeanAngle(const a:tAngles;cnt:longInt):double;
// calcualtes mean angle.
// returns 0.0 if direction is not sure.
const
  eps = 1e-10;

var 
  i : longInt;
  s,c,
  Sumsin,SumCos : extended;
begin
  if cnt = 0 then
    begin
      MeanAngle := 0.0;
      exit;
    end;

    SumSin := 0;
    SumCos := 0;
    for i := Cnt -1 downto 0 do
      begin
        sincos(DegToRad(a[i]),s,c);
        Sumsin := sumSin + s;
        SumCos := sumCos + c;
      end;
      s := SumSin/cnt;
      c := SumCos/cnt;
      if c > eps then
        MeanAngle := RadToDeg(arctan2(s,c))
      else
        // Not meaniingful
        MeanAngle := 0.0;
end;

procedure OutMeanAngle(const a:tAngles; cnt: longInt);
var 
  i : longInt;
begin
  if cnt > 0 then
    begin
      write('The mean angle of [');
      for i := 0 to Cnt-2 do
        write(a[i]:0:2, ',');
      write(a[Cnt-1]:0:2,'] => ');
      writeln(MeanAngle(a,cnt):0:16);
    end;
end;

var
  a:tAngles;
begin
  setlength(a,4);

  a[0] := 350;a[1] := 10;
  OutMeanAngle(a,2);
  a[0] := 90;a[1] := 180;a[2] := 270;a[3] := 360;
  OutMeanAngle(a,4);
  a[0] := 10;a[1] := 20;a[2] := 30;
  OutMeanAngle(a,3);

  setlength(a,0);
end.




