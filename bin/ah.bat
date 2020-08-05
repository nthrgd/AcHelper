@echo off
set /p op=Choissisez le mode que vous souhaitez : 

set modify=0
if %op%==m set modify=1
if %op%==modif set modify=1
if %op%==modifier set modify=1

if %modify%==1 (
	scripts\modify.bat
)

set new=0
if %op%==n set new=1
if %op%==nouv set new=1
if %op%==nouveau set new=1

if %new%==1 (
	scripts\new.bat
)

echo Fin.
pause > nul