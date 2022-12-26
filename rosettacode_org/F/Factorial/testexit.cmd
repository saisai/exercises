@PowerShell -NonInteractive -NoProfile -Command "& {./exit.ps1; exit $LastExitCode }"
@echo From Cmd.exe: Exit.ps1 exited with exit code %errorlevel%