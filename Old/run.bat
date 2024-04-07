@echo off

:: Change to the directory where the batch file is located
cd /d %~dp0

:: Set the relative path to the virtual environment
set VIRTUAL_ENV=%~dp0venv

:: Activate the virtual environment
call %VIRTUAL_ENV%\Scripts\activate

:: Check for PSSecurityException and adjust execution policy if needed
powershell -Command "& { try { python -c 'exit()' } catch { if ($_.Exception.FullyQualifiedErrorId -eq 'UnauthorizedAccess') { Set-ExecutionPolicy RemoteSigned -Scope Process } } }"

:: Run the Python script
python main.py

:: Pause to allow user input (press any key to continue)
pause
