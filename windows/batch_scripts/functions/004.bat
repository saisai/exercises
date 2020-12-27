@echo off
set str=Outer
echo %str%
call :SetValue str
echo %str%
exit /b %errorlevel%

:SetValue
 setlocal
 set str=Inner
 set "%~1=%str%"
 endlocal
 exit /b 0
