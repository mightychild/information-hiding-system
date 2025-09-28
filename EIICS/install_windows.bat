@echo off
echo Installing EIICS with icons...
pip install dist\eiics-1.0.0-py3-none-any.whl

:: Create desktop shortcut (optional)
echo Creating desktop shortcut...
echo [Desktop Shortcut] > "%USERPROFILE%\Desktop\EIICS.lnk"
echo URL=eiics >> "%USERPROFILE%\Desktop\EIICS.lnk"

echo Installation complete!
pause