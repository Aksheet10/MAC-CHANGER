#!/usr/bin/python3
import os
try:
    os.system("pip3 install pyfiglet")
    import pyfiglet
except KeyboardInterrupt:
    print("[ERR] Caught Keyboard Interrupt. Exiting... [ERR]")
try:
    import termcolor
except:
    os.system('pip3 install termcolor')
from termcolor import colored
import time
try:
    os.system('clear')
except KeyboardInterrupt:
    print('\n[-] You interrupted the program')
print((colored(pyfiglet.figlet_format('MAC-Changer', font='slant'), color='green')))
print((colored('='*50, color='green')))
print((colored('\t[+] Mac changer for LINUX ONLY', color='green')))
print((colored('\t[+] Built on 20 October 2020', color='green')))
print((colored('\t[+] Built by Aksheet', color='green')))
print((colored('='*50 + '\n\n', color='green')))


def chk_inter():
    #  program to check for interface
    chk = input((colored('Do you want to check interfaces? (y/n): ',  color='green')))
    if chk == 'y:
        os.system('ifconfig')
    elif chk == 'n':
        print((colored('Lets assume you know the interface :)\n',  color='green')))
        pass
    else:
        print((colored('Please enter "y" or "n"\n',  color='red')))
        chk_inter()


def change():
    #  program to change MAC address
    time.sleep(3)  # sleep for 3 seconds
    chk_inter()
    sel_inter = input((colored('\n[+] Please enter a interface(eg:eth0): ',  color='green')))  # interface input
    mac_change = input((colored('[+] Enter the new MAC (ff:ff:ff:ff:ff:ff) Start with 00. \nExample >> 00:11:22:33:44:55 \n>> ',  color='green')))

    os.system('sudo ifconfig ' + sel_inter + ' down')
    os.system('sudo ifconfig ' + sel_inter + ' hw' + ' ether ' + mac_change)
    os.system('sudo ifconfig ' + sel_inter + ' up')
    time.sleep(1)
    print((colored("\n[+] MAC for " + sel_inter + " changed successfully to " + mac_change,  color='green')))

    def check():
        chk_res = input((colored('\nDo you want to check the MAC for ' + sel_inter + '? (y/n): ',  color='green')))
        time.sleep(1)
        if chk_res == 'y:
            print('\n')
            os.system('ifconfig ' + sel_inter + '\n')
        elif chk_res == 'n':
            print((colored('\nNot checking MAC address\n',  color='green')))
        else:
            print((colored('Please enter "y" or "n"',  color='red')))
            check()
    check()

    def restore():
        ask = input((colored('\nDo you want to restore the MAC address of ur interface (r) or exit (e) (r/e)?: ',  color='green')))
        time.sleep(1)
        if ask == 'r':

            def rmc():
                conf = input((colored('\nDo you want to restore MAC (y/n): ',  color='green')))
                time.sleep(1)
                if conf == 'y':
                    os.system(f'ifconfig {sel_inter} down')
                    os.system(f'macchanger -p {sel_inter}')
                    os.system(f'ifconfig {sel_inter} up')

                    print((colored('\n[+] MAC restored',  color='green')))

                elif conf == 'n':
                    def not_change():
                        print((colored('\n[-] Not changing MAC address',  color='green')))
                        time.sleep(1)
                        cn = input((colored('\nDo you want to check if MAC changed or not? (y/n)?: ',  color='green')))
                        print('\n')
                        time.sleep(1)
                        if cn == 'y':
                            print('\n')
                            os.system(f'ifconfig {sel_inter}')
                        elif cn == 'n':
                            print((colored('\nMAC did not restore :) ',  color='green')))
                        else:
                            print((colored('Please enter "y" or "n"',  color='red')))
                            not_change()
                    not_change()

                else:
                    print((colored('Please enter "y" or "n"',  color='red')))
                    rmc()
            rmc()

        elif ask == 'e':
            print((colored('\n[-] Exiting\n',  color='red')))
        else:
            print(colored('Please enter "r" or "e"',  color='red'))
            restore()
    restore()


try:
    change()
except:
    print()
    print((colored('\n[-] You quit the program :(\n',  color='red')))
