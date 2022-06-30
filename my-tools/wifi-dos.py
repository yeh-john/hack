### REFERENCE : https://github.com/crypt0b0y/BLUETOOTH-DOS-ATTACK-SCRIPT/blob/master/Bluetooth-DOS-Attack.py
#Start import
import os
import time

# ANSI color code :  https://stackoverflow.com/questions/3585846/color-text-in-terminal-applications-in-unix
def printLogo():
    print('\x1b[31m')
    print('                             WIFI DOS Script       MADE BY : yeh-john                              ')
    print('+------------------------------------------------------------------------------------------------+ ')
    print('|     :::       ::: ::::::::::: :::::::::: :::::::::::          :::::::::   ::::::::   ::::::::  | ')
    print('|    :+:       :+:     :+:     :+:            :+:              :+:    :+: :+:    :+: :+:    :+:  | ')
    print('|   +:+       +:+     +:+     +:+            +:+              +:+    +:+ +:+    +:+ +:+          | ')
    print('|  +#+  +:+  +#+     +#+     :#::+::#       +#+              +#+    +:+ +#+    +:+ :#:           | ')
    print('| +#+ +#+#+ +#+     +#+     +#+            +#+              +#+    +#+ +#+    +#+ +#+   +##+#    | ')
    print('| #+#+# #+#+#      #+#     #+#            #+#              #+#    #+# #+#    #+# #+#      #      | ')
    print('| ###   ###   ########### ###        ###########          #########   ########   ########        | ')
    print('+------------------------------------------------------------------------------------------------+ ')
    print('\x1b[0m') # Reset text color

# Main code
def main():
    printLogo()
    time.sleep(0.1)
    print('')
    # Ask permision
    print('\x1b[32m USE OF THIS SOFTWARE IS AT YOUR OWN RISK. THE DEVELOPER SHALL NOT BE LIABLE FOR ANY DAMAGES RESULTING FROM THE USE OF THIS SOFTWARE.')
    if (input("Do you agree? [Y/n] >") in ['Y','y']):
        time.sleep(0.1)
        os.system('clear')
        printLogo()
        print('')

        #### Start prigram
        # Ask target BSSID
        target_id = input("Enter target BSSID >")
        if len(target_id) < 1:
            print("[!] ERROR : Target BSSID error")
            exit(0)
        
        # Ask dos ammount
        dos_amt = input("default[10000] Enter DOS amount >")
        if dos_amt == "":
            dos_amt = 10000
        ### test ###
        elif len(dos_amt) < 1:
            print("[!] ERROR : Dos amount error")
            exit(0)
            
       ### FIX LINK ###
       # https://stackoverflow.com/questions/20652527/python-try-except-with-of-if-else
        
# Start command
if __name__ == '__main__':
    try:
        os.system('clear')
        main()
    # Error doing something
    except KeyboardInterrupt:
        time.sleep(0.1)
        print('\n[*] Aborted')
        exit(0)
    # Print error info
    except Exception as e:
        time.sleep(0.1)
        print('[!] ERROR: ' + str(e))
