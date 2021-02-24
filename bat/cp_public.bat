@echo off
set from_path1=D:\tvkoo\projectx\release\server\bin
set copy_path1=D:\tvkoo\projectx\release\server\public_bin
echo copy config
echo from: 	%from_path1%\config
echo To: 	%copy_path1%\config
echo.
copy %from_path1%\config\*.* %copy_path1%\config\ >nul
echo.

set copy_obj=gamesrv.exe
echo copy exe
echo from: 	%from_path1%
echo To: 	%copy_path1%
echo Obj:	%copy_obj%
echo.
for  %%I in (%copy_obj%) do (
::echo %from_path1%\%%I
copy %from_path1%\%%I %copy_path1%\%%I >nul
)
echo.


::pause

