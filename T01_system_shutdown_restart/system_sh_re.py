# this script used to shutdown or restart your operating system.

import os

def system_sh_re():
    print("Enter 'r' or 'R' for restart")
    print("Enter 's' or 'S' for shutdown")
    print("Enter any else 'key' for exit")

    option = input("Enter your option: ")
    if option == 's' or option == 'S':
        os.system('shutdown /s')
    elif option == 'r' or option == 'R':
        os.system('shutdown /r')
    else:
        print('exit')
        exit()

system_sh_re()

    
