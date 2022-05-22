@echo off
echo English:
echo you are about to install loggepy .
echo if it is your will you can continue.
echo.
echo.
echo.
echo Francais:
echo vous etes sur le point d'installer loggepy .
echo si c'est votre volonte vous pouvez continuer.
pause
cls

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

cls


for /f "delims=" %%a in ('dir . /b/s ^| findstr /R "\\loggepy$" ')  do set "paths=%%~dpnxa"

cd C:\Program Files (x86)
mkdir loggepy
xcopy "%paths%" "C:\Program Files (x86)\loggepy"

echo 10% loading
echo [**********\                                                                                          /]

cd C:\Program Files (x86)\loggepy
mkdir Script
xcopy "%paths%\Script" "C:\Program Files (x86)\loggepy\Script"

cd C:\Program Files (x86)\loggepy
mkdir log
xcopy "%paths%\log" "C:\Program Files (x86)\loggepy\log"

echo 30% loading
echo [******************************\                                                                      /]

cd C:\ProgramData
mkdir passworld_loggepy


cd C:\Program Files (x86)\loggepy
del update.bat /s /q

cd C:\Users\%USERNAME%\AppData\Roaming
mkdir loggepy
xcopy "%paths%\update.bat" "C:\Users\%USERNAME%\AppData\Roaming\loggepy"


set SCRIPT="%TEMP%\%RANDOM%-%RANDOM%-%RANDOM%-%RANDOM%.vbs"

echo Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%
echo sLinkFile = "%USERPROFILE%\Desktop\launcher loggepy.lnk" >> %SCRIPT%
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%
echo oLink.TargetPath = "C:\Program Files (x86)\loggepy\launcher.bat" >> %SCRIPT%
echo oLink.Save >> %SCRIPT%

cscript /nologo %SCRIPT%
del %SCRIPT%

echo 50% loading
echo [**************************************************\                                                  /]
echo please wait

python -m pip install pyfade==3.1
python -m pip install keyboard==0.13.5
python -m pip install python-dotenv==0.19.0
python -m pip install pyperclip==1.8.2
python -m pip install requests==2.27.1
python -m pip install bs4==0.0.1

echo 100% loading complite
echo [****************************************************************************************************]
pause

cd %~dp0
rd loggepy /s /q
del README.md /s /q

cd %~dp0
del setup.bat