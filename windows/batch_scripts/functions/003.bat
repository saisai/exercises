@echo off
setlocal
call :SetValue value1,value2
echo %value1%
echo %value2%
exit /b %errorlevel%

:SetValue
 set "%~1=5"
 set "%~2=10"
 exit /b 0
