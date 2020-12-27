@echo off
setlocal
call :Display 5, 10
exit /b %errorlevel%

:Display
	echo the value of parameter 1 is %~1
	echo the value of parameter 2 is %~2
	exit /b 0
