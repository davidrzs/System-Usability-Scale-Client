main: main.py
	pyinstaller main.py --add-data 'templates:templates' --onefile

