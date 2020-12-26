@echo off
setlocal
set "list=a b c d"
(
 for %%i in (%list%) do (
  echo(%%i
  echo(
 )
)>file.txt