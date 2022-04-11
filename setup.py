#KingOfMongeese

import platform
import os

system = platform.system()

try:
    import tkinter
    print('tkinter found')

except:
    print('Failed dependancy...tkinter\nInstalling tkinter')
    if system == 'Windows':
        os.system('pip install tkinter')
        print('tkinter installed')
        print('setup complete')
    elif system == 'Linux':
        print('Please run the following commands to install tkinter:')
        print('  sudo apt update \n  sudo apt install python3-tk')
        install = input('Run commands now? You will need to enter sudo password.(y/n)').strip().lower()
        if install.startswith('y'):
            os.system('sudo apt update && sudo apt install python3-tk')
            

try:
    import tkinter
    print('All dependancies met. \nSetup complete')
except:
    print('Setup incomplete. Try running again.')
    print('Your OS may not be supported by this script')


    

   
    
