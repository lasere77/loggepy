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

cd C:\Program Files (x86)\loggepy
rd Script /s /q
echo.
echo uninstallation of scripts success !!!


cd C:\Program Files (x86)\loggepy
mkdir Script
xcopy "C:\Windows\Temp\loggepy_update\loggepy\loggepy\Script" "C:\Program Files (x86)\loggepy\Script" /e /i
echo.
echo end of the installation of the new modules.

cd C:\Program Files (x86)\loggepy
del uninstall.bat /s /q
del launcher.bat /s /q
del README.md /s /q

xcopy "C:\Windows\Temp\loggepy_update\loggepy\loggepy\uninstall.bat" "C:\Program Files (x86)\loggepy"
xcopy "C:\Windows\Temp\loggepy_update\loggepy\loggepy\launcher.bat" "C:\Program Files (x86)\loggepy"
xcopy "C:\Windows\Temp\loggepy_update\loggepy\loggepy\README.md" "C:\Program Files (x86)\loggepy"

cls
pause