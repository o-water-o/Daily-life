@echo off
if not exist log (
	md log
	echo create folder log )

echo run in backstage
choice /t 2 /d y /n >null
if "%1" == "h" goto begin 
    mshta vbscript:createobject("wscript.shell").run("%~nx0 h",0)(window.close)&&exit 
:begin 
set ymd=%date:~0,4%%date:~5,2%%date:~8,2%
set hour=%TIME:~0,2%
set min=%TIME:~3,2%
echo ####################################>>log/%ymd%.txt
echo time:%ymd% %hour%:%min%>>log/%ymd%.txt
start "v2ray" /b v2ray.exe >>log/%ymd%.txt
echo ------------------------------------>>log/%ymd%.txt