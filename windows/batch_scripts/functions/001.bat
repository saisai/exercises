
@echo off
setlocal
call :Display
exit /b %errorlevel%

:Display
	set /a index=2
	echo the value of index is %index%
	exit /b 0
