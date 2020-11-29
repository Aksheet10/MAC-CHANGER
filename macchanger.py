#!/usr/bin/python3
import subprocess
import os
try:
    import pyfiglet
except:
    os.system("pip3 install pyfiglet")
except KeyboardInterrupt:
    print("[ERR] Caught Keyboard Interrupt. Exitting... [ERR]")
import time
try:
    os.system('clear')
except KeyboardInterrupt:
    print('\n[-] You interrupted the program')
print(pyfiglet.figlet_format('MAC-Changer', font='slant'))
print('='*50)
print('\t[+] Mac changer for LINUX ONLY')
print('\t[+] Built on 20 October 2020')
print('\t[+] Built by Aksheet')
print('='*50 + '\n\n')


def chk_inter():
    #  program to check for interface
    chk = input('Do you want to check interfaces? (y/n): ')
    if 'y' in chk:
        subprocess.run(['ifconfig'], shell=True)
    elif 'n' in chk:
        print('Lets assume you know the interface :)')
        pass
    else:
        print('Please enter "y" or "n"')
        chk_inter()


def change():
    #  program to change MAC address
    time.sleep(3)  # sleep for 3 seconds
    chk_inter()
    sel_inter = input('\n[+] Please enter a interface(eg:eth0): ')  # interface input
    mac_change = input('[+] Enter the new MAC (ff:ff:ff:ff:ff:ff) Start with 00. \nExample >> 00:11:22:33:44:55 \n>> ')

    os.system('sudo ifconfig ' + sel_inter + ' down')
    os.system('sudo ifconfig ' + sel_inter + ' hw' + ' ether ' + mac_change)
    os.system('sudo ifconfig ' + sel_inter + ' up')
    time.sleep(1)
    print("\n[+] MAC for " + sel_inter + " changed successfully to " + mac_change)

    def check():
        chk_res = input('\nDo you want to check the MAC for ' + sel_inter + '? (y/n): ')
        time.sleep(1)
        if 'y' in chk_res:
            print('\n')
            os.system('ifconfig ' + sel_inter + '\n')
        elif 'n' in chk_res:
            print('\nSure\n')
        else:
            print('Please enter "y" or "n"')
            check()
    check()

    def restore():
        ask = input('Do you want to restore the MAC address of ur interface (r) or exit (e) (r/e)?: ')
        time.sleep(1)
        if 'r' in ask:

            def rmc():
                conf = input('\nDo you want to restore MAC (y/n): ')
                time.sleep(1)
                if 'y' in conf:
                    os.system(f'ifconfig {sel_inter} down')
                    os.system(f'macchanger -p {sel_inter}')
                    os.system(f'ifconfig {sel_inter} up')

                    print('\n[+] MAC restored')

                elif 'n' in conf:
                    def not_change():
                        print('\n[-] Not changing MAC address ')
                        time.sleep(1)
                        cn = input('\nDo you want to check if MAC changed or not? (y/n)?: ')
                        print('\n')
                        time.sleep(1)
                        if 'y' in cn:
                            print('\n')
                            os.system(f'ifconfig {sel_inter}')
                        elif 'n' in cn:
                            print('\nMAC did not restore :) ')
                        else:
                            print('Please enter "y" or "n"')
                            not_change()
                    not_change()

                else:
                    print('Please enter "y" or "n"')
                    rmc()
            rmc()

        elif 'e' in ask:
            print('\n[-] Exiting\n')
        else:
            print('Please enter "r" or "e"')
            restore()
    restore()


try:
    change()
except:
    print('\n[-] You quit the program :(\n')
