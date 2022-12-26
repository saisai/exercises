@echo off
set number=1
:loop
set /a number+=1
echo %number%
goto loop

pause>nul
