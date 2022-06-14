@echo off

echo ha it looks like the dependencies were not installed
echo check that you are well connected to the internet and thank you for your patience
pause
python -m pip install pyfade==3.1
python -m pip install keyboard==0.13.5
python -m pip install python-dotenv==0.19.0
python -m pip install pyperclip==1.8.2
python -m pip install requests==2.27.1
python -m pip install bs4==0.0.1

cls
cd C:\Program Files (x86)\loggepy
python Script\loggepy.py
exit
pause>nul