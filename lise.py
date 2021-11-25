#!/usr/bin/python3
#-*-coding:utf-8-*-
# Made With ❤️ UJ
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess,elite1

def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")
    else:os.system("clear")
def banner():
        print ('\x1b[1;91m         ____ _____ __  __  ___   ___\n\x1b[1;91m        |  _ \\___ /|  \\/  |/ _ \\ / _ \\\n\x1b[1;92m        | | | ||_ \\| |\\/| | | | | (_) |\n\x1b[1;92m        | |_| |__) | |  | | |_| |\\__, |\n\x1b[1;91m        |____/____/|_|  |_|\\___/   / /\n\x1b[1;91m                                  / /\n\x1b[1;97m-------------------------------------------------')

def spt():
	try:
		toket = open('licensed.log','r').read()
	except IOError:
		print("\x1b[91m  License Invalid\x1b[0m !");time.sleep(2)
		clear()
		os.system('rm -rf licensed.log')
		user()
	if os.path.exists('licensed.log'): 
		user1()
		#user()
	else:
		user()
		##user1()
def user():
    clear()
    banner()
    print(45*"_")
    print ('  [+]Generating ID ...');time.sleep(3)
    print ("  [+]SUCCES");time.sleep(0.07)
    liid = uuid.uuid4().hex[:25] ## hex 20 change to 25
    idg = open('licensed.log', 'w')
    idg.write(liid)
    idg.close()
    print ("  [+]YOUR PREMIUM KEY : "+ liid);time.sleep(0.07)
    print ("  [+]Dont forgot your key");time.sleep(0.07)
    print ("  [+]Your KEY Has Not Been Confirmed");time.sleep(0.07)
    print ("  [+]Please Contact Admin for ID Confirmation");time.sleep(0.07)
    print ("  [+]Use Free Version Till ADMIN Confirm Your License Key");time.sleep(0.07)
    input ("  Press Enter to Chat Admin");time.sleep(0.07)
    os.system('am start https://wa.me/994405023452?text=bro,+I+want+to+buy+the+premium,+this+is+my+premium+license+key:%20' + liid + ' >/dev/null')
    time.sleep(1)
    os.sys.exit(elite1.menu())
def user1():
    try:
      clear()
      banner()
      j = input(" [+] Enter Your License key(must be 25 characters: ")
      r = requests.get("https://github.com/Sahanuj/Ujbf/blob/main/Uj/li.txt").text
      if len(j)!=25:print("key must be 25 characters").exit()
      else:pass
      if j in r:
          print("  Please Wait .. Checking Your Key !");time.sleep(3)
          clear()
          banner()
          print("  Login Status : \x1b[92mComplete\x1b[0m")
          time.sleep(1)
          os.sys.exit(elite1.menu())
      else:
          clear()
          banner()
          print ("  [!]Login Status :\x1b[91m Failed \x1b[0m");time.sleep(0.07)
          print ("  [+]ID Not Confirmed");time.sleep(0.07)
          print ("  [+]Please Chat Admin For Confirmed Your ID");time.sleep(0.07)
          print ("  [+]Use Free Version Till ADMIN Confirm Your License Key");time.sleep(0.07)
          input ("  Press Enter To Chat Admin");time.sleep(0.07)
          idgg = open('licensed.log', 'R').read()
          os.system('am start https://wa.me/994405023452?text=bro,+I+want+to+buy+the+premium,+this+is+my+premium+license+key:%20' + idgg + ' >/dev/null')
          time.sleep(1)
          os.sys.exit(elite1.menu())
    except requests.exceptions.ConnectionError:
      print ('  \x1b[91mNo Connection')
      input('  \x1b[0m Back')
      spt()
    except KeyboardInterrupt:
      os.sys.exit()
    except IOError:
      subprocess.Popen(['rm', '-rf', 'licensed.log'])
      user()