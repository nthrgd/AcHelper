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

set refresh=0
if %op%==r set refresh=1
if %op%==refresh set refresh=1

if %refresh%==1 (
	scripts\refresh.bat
)

set version=0
if %op%==v set version=1
if %op%==version set version=1
if %version%==1 (
	scripts\version.bat
)

echo Fin.
pause > nul