#coding: utf-8
#██████╗ ███████╗██╗   ██╗███████╗██╗      ██████╗ ██████╗ ███████╗██████╗     ██████╗ ██╗   ██╗    ██████╗ ███████╗███████╗██╗   ██╗██████╗  ██████╗      ██╗  ██╗
#██╔══██╗██╔════╝██║   ██║██╔════╝██║     ██╔═══██╗██╔══██╗██╔════╝██╔══██╗    ██╔══██╗╚██╗ ██╔╝    ██╔══██╗██╔════╝██╔════╝██║   ██║██╔══██╗██╔═══██╗     ╚██╗██╔╝
#██║  ██║█████╗  ██║   ██║█████╗  ██║     ██║   ██║██████╔╝█████╗  ██║  ██║    ██████╔╝ ╚████╔╝     ██████╔╝███████╗█████╗  ██║   ██║██║  ██║██║   ██║█████╗╚███╔╝ 
#██║  ██║██╔══╝  ╚██╗ ██╔╝██╔══╝  ██║     ██║   ██║██╔═══╝ ██╔══╝  ██║  ██║    ██╔══██╗  ╚██╔╝      ██╔═══╝ ╚════██║██╔══╝  ██║   ██║██║  ██║██║   ██║╚════╝██╔██╗ 
#██████╔╝███████╗ ╚████╔╝ ███████╗███████╗╚██████╔╝██║     ███████╗██████╔╝    ██████╔╝   ██║       ██║     ███████║███████╗╚██████╔╝██████╔╝╚██████╔╝     ██╔╝ ██╗
#╚═════╝ ╚══════╝  ╚═══╝  ╚══════╝╚══════╝ ╚═════╝ ╚═╝     ╚══════╝╚═════╝     ╚═════╝    ╚═╝       ╚═╝     ╚══════╝╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝      ╚═╝  ╚═╝
#!/usr/bin/python

import os
import sys
import getpass
import smtplib


filtechColorGrey = '\033[40m'
filtechColorLightGrey = '\033[40m'

if len(sys.argv) < 2:
    os.system("cls||clear")
    sys.stdout.write(filtechColorGrey+"""
                                    $$$$$$$$\ $$$$$$\ $$\    $$$$$$$$\ $$$$$$$$\  $$$$$$\  $$\   $$\                                 
                                    $$  _____|\_$$  _|$$ |   \__$$  __|$$  _____|$$  __$$\ $$ |  $$ |                                
                                    $$ |        $$ |  $$ |      $$ |   $$ |      $$ /  \__|$$ |  $$ |                                
                                    $$$$$\      $$ |  $$ |      $$ |   $$$$$\    $$ |      $$$$$$$$ |                                
                                    $$  __|     $$ |  $$ |      $$ |   $$  __|   $$ |      $$  __$$ |                                
                                    $$ |        $$ |  $$ |      $$ |   $$ |      $$ |  $$\ $$ |  $$ |                                
                                    $$ |      $$$$$$\ $$$$$$$$\ $$ |   $$$$$$$$\ \$$$$$$  |$$ |  $$ |                                
                                    \__|      \______|\________|\__|   \________| \______/ \__|  \__|                                
$$$$$$$$\ $$\      $$\  $$$$$$\  $$$$$$\ $$\              $$$$$$\  $$$$$$$\   $$$$$$\  $$\      $$\ $$\      $$\ $$$$$$$$\ $$$$$$$\  
$$  _____|$$$\    $$$ |$$  __$$\ \_$$  _|$$ |            $$  __$$\ $$  __$$\ $$  __$$\ $$$\    $$$ |$$$\    $$$ |$$  _____|$$  __$$\ 
$$ |      $$$$\  $$$$ |$$ /  $$ |  $$ |  $$ |            $$ /  \__|$$ |  $$ |$$ /  $$ |$$$$\  $$$$ |$$$$\  $$$$ |$$ |      $$ |  $$ |
$$$$$\    $$\$$\$$ $$ |$$$$$$$$ |  $$ |  $$ |            \$$$$$$\  $$$$$$$  |$$$$$$$$ |$$\$$\$$ $$ |$$\$$\$$ $$ |$$$$$\    $$$$$$$  |
$$  __|   $$ \$$$  $$ |$$  __$$ |  $$ |  $$ |             \____$$\ $$  ____/ $$  __$$ |$$ \$$$  $$ |$$ \$$$  $$ |$$  __|   $$  __$$< 
$$ |      $$ |\$  /$$ |$$ |  $$ |  $$ |  $$ |            $$\   $$ |$$ |      $$ |  $$ |$$ |\$  /$$ |$$ |\$  /$$ |$$ |      $$ |  $$ |
$$$$$$$$\ $$ | \_/ $$ |$$ |  $$ |$$$$$$\ $$$$$$$$\       \$$$$$$  |$$ |      $$ |  $$ |$$ | \_/ $$ |$$ | \_/ $$ |$$$$$$$$\ $$ |  $$ |
\________|\__|     \__|\__|  \__|\______|\________|       \______/ \__|      \__|  \__|\__|     \__|\__|     \__|\________|\__|  \__|

\n"""+filtechColorLightGrey)

else:
    sys.exit("Usage: python filtech-spammer.py")
    os.system("cls||clear")

print("[ How to use in Computer : python FiltechSpammer.py ] \n")
print("[ How to use in Termux : python2 FiltechSpammer.py ] \n")

filtechEmail = raw_input("Please Enter your Email Address Here :")
filtechPassword = getpass.getpass("Enter your Password :")
filtechVictim = raw_input("Victim Email Address : ")
filtechMessage = raw_input("Your Message to your Victim : ")
filtechSpam = int(input("Spam Count :"))

try:
    filtech_smtp = 'smtp.gmail.com'
    filtechPort = 587

    filtechServer = smtplib.SMTP(filtech_smtp,filtechPort)
    filtechServer.ehlo()
    filtechServer.starttls()
    filtechServer.login(filtechEmail, filtechPassword)

    print("[-] // Spamming .......... Please Wait ...... [-] \n")

    filtech = 0
    while filtech < filtechSpam:
        filtech += 1
        filtechServer.sendmail(filtechEmail,filtechVictim, filtechMessage)
    if filtech == 1:
        print(" %dst Email Successfully Sent!" % (filtech))
    elif filtech == 2:
        print(" %dnd Email Successfully Sent!" % (filtech))
    elif filtech == 3:
        print(" %drd Email Successfully Sent!" % (filtech))
    else:
        print(" %dth Email Successfully Sent!" % (filtech))
    sys.stdout.flush()
    filtechServer.quit()
    print("Spamming Done!")

except KeyboardInterrupt:
    print()
    print("Canceled [X]")
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print("The username or password did you entered is incorrect")
    print("or Check your Gmail option if 'Less Secure' is enable to use this Spammer. ")
    sys.exit()
