@echo off

:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
    IF "%PROCESSOR_ARCHITECTURE%" EQU "amd64" (
>nul 2>&1 "%SYSTEMROOT%\SysWOW64\cacls.exe" "%SYSTEMROOT%\SysWOW64\config\system"
) ELSE (
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
)

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params= %*
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params:"=""%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
:--------------------------------------


echo uninstall loggepy ?
echo.
echo desinstaller loggepy ?
pause
echo uninstall "C:\ProgramData\passworld_loggepy"
cd C:\ProgramData
rd passworld_loggepy /s /q
echo loggepy has been uninstalled

echo uninstall "C:\Users\%USERNAME%\AppData\Roaming\loggepy"
cd C:\Users\%USERNAME%\AppData\Roaming
rd loggepy /s /q

echo uninstall "C:\Users\%USERNAME%\Desktop\launcher loggepy"
cd C:\Users\%USERNAME%\Desktop
rd launcher loggepy.lnk /s /q

echo uninstall "cd C:\Program Files (x86)\loggepy"
cd C:\Program Files (x86)
rd loggepy /s /q
pause