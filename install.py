#python3
from subprocess import call
import platform

toInstall = ['tinydb', 'flask', 'flask_session', 'pyinstaller']

def main():
    system = platform.system()
    if system == 'Linux' or system == 'Darwin':
        for item in toInstall:
            call(['pip3', 'install', str(item)])
    if system == 'Windows':
        for item in toInstall:
            call(['pip', 'install', str(item)])

if __name__== "__main__":
  main()