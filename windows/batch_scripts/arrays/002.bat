@echo off 

set list=1 2 3 4
(
for %%i in (%list%) do ( 
   echo %%i
)
)