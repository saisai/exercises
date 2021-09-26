@echo off

::for /f %%i in (file.txt) do if %%i@ neq @ echo %%i
::for /f %%i in (file.txt) do echo %%i

for /F "tokens=*" %%A in (file.txt) do echo %%A

