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

██╗  ██╗     ██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
╚██╗██╔╝     ██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
 ╚███╔╝█████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
 ██╔██╗╚════╝██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
██╔╝ ██╗     ██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
╚═╝  ╚═╝     ╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
    Created by Pseudo-X [2019 Spammer Tool - Re-developed ]

\n"""+filtechColorLightGrey)

else:
    sys.exit("Usage: python filtech-spammer.py")
    os.system("cls||clear")

print("[ How to use in Computer : python FiltechSpammer.py ] \n")
print("[ How to use in Termux : python2 FiltechSpammer.py ] \n")

sudoEmail = input("Please Enter your Email Address Here :")
sudoPassword = getpass.getpass("Enter your Password :")
sudoVictim = input("Victim Email Address : ")
sudoMessage = input("Your Message to your Victim : ")
sudoSubject = input("Enter Subject : ")
sudoMessageSubmit = 'Subject: {}\n\n{}'.format(sudoSubject, sudoMessage)
sudoSpam = int(input("Spam Count :"))

try:
    filtech_smtp = 'smtp.gmail.com'
    filtechPort = 587

    filtechServer = smtplib.SMTP(filtech_smtp,filtechPort)
    filtechServer.ehlo()
    filtechServer.starttls()
    filtechServer.login(sudoEmail, sudoPassword)

    print("[-] // Spamming .......... Please Wait ...... [-] \n")

    filtech = 0
    while filtech < sudoSpam:
        filtech += 1
        filtechServer.sendmail(sudoEmail, sudoVictim, sudoMessageSubmit)
    if filtech == 1:
        print(" %dst Email Sent Successfully!" % (filtech))
    elif filtech == 2:
        print(" %dnd Email Sent Successfully!" % (filtech))
    elif filtech == 3:
        print(" %drd Email Sent Successfully!" % (filtech))
    else:
        print(" %dth Email Sent Successfully!" % (filtech))
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
