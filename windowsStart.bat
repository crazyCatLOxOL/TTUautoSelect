if not exist "%CD%\venvWindows" (
	python -m venv "%CD%\venvWindows"
	call "%CD%\venvWindows\scripts\activate.bat"
	python -m pip install pyqt5
	python -m pip install requests
	python -m pip install lxml
) else (
	call "%CD%\venvWindows\scripts\activate.bat"
)
set QT_QPA_PLATFORM_PLUGIN_PATH=%CD%\venvWindows\Lib\site-packages\PyQt5\Qt\plugins\platforms
cd src

python "%CD%\main.py" 2> ..\error.txt
