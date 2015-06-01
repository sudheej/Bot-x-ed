#!/usr/bin/python
import cleverbot
import os
import aiml
import sys, traceback
def main():
    try:
	newCbSession1=cleverbot.Session()
	# Create a Kernel object.
	kern = aiml.Kernel()
	os.system('clear')
	brainLoaded = False
	forceReload = False
	print "\033[95m" + "Welcome to The Bot Talk"
	print "-------------------------------"
	while not brainLoaded:
		if forceReload or (len(sys.argv) >= 2 and sys.argv[1] == "reload"):
			kern.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
			brainLoaded = True
			kern.saveBrain("standard.brn")

		else:
			try:
				kern.bootstrap(brainFile = "standard.brn")
				brainLoaded = True
			except:
				forceReload = True
	os.system('clear')
	print "Created by Sudheej a.k.a XtechKid"
	print "Bot Conversation Mode (ctrl-c to exit)"
	subject = raw_input("Enter a conversation subject :")
	flag = True
	while True:
		if flag:
			bot1_respon = newCbSession1.Ask(subject)
			print '\033[94m' + "Bot1 : %s" %bot1_respon + '\033[0m'
			bot2_respon = kern.respond(bot1_respon)		
			print '\033[92m' + "Bot2 : %s" %bot2_respon + '\033[0m'
			flag = False
		else:
			bot1_respon = newCbSession1.Ask(bot2_respon)
			print '\033[94m' + "Bot1 : %s" %bot1_respon + '\033[0m'
			bot2_respon = kern.respond(bot1_respon)	
			print '\033[92m' + "Bot2 : %s" %bot2_respon + '\033[0m'

    except KeyboardInterrupt:
        print "Shutdown requested...exiting"
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

if __name__ == "__main__":
    main()
