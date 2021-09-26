@echo off

::setting variables in different ways
set myInt1=5
set myString=Roseete Code
set "myInt2=5"
set "myString2=Roseete Code"

:: Arithmetic
set /a myInt1=%myInt1%+1
set /a myInt2+=1
set /a myint3=myInt2+   4

set myInt
set myString
pause>nul
