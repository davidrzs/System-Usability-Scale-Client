main: main.py
	pyinstaller main.py --add-data 'templates;templates' --onefile --name sus

# on windows use 'templates;templates' instead of 'templates:templates'
