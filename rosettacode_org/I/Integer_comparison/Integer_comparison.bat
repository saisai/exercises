@echo off
setlocal enabledelayedexpansion
set /p a="A: "
set /p b="B: "
if %a%  lss %b% (
    echo %a% is less than %b%
) else ( if %a% gtr %b% (
    echo %a% is greater than %b%
    ) else ( if %a% equ %b% (
    echo %a%a is equal to %b%
)))

pause>nul