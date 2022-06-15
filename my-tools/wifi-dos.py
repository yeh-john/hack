### REFERENCE : https://github.com/crypt0b0y/BLUETOOTH-DOS-ATTACK-SCRIPT/blob/master/Bluetooth-DOS-Attack.py
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





if __name__ == '__main__':
    try:
        os.system('cls')
        main()
    except KeyboardInterrupt:
        time.sleep(0.1)
        print('\n[*] Aborted')
        exit(0)
    except Exception as e:
        time.sleep(0.1)
        print('[!] ERROR: ' + str(e))
