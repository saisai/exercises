@echo off
set /p x=
set /a fs=%x%-1
set y=%x%
for /l %%a in (%fs%, -1, 1) do set /a y*=%%a
if %x% equ 0 set y=1
echo %y%
pause
::exit
