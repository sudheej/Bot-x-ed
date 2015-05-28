#!/usr/bin/python
import cleverbot
import os
newCbSession1=cleverbot.Session()
newCbSession2=cleverbot.Session()
os.system('clear')
print "\033[95m" + "Welcome to The Bot Talk"
print "-------------------------------"
print "Created by Sudheej"
subject = raw_input("Enter a conversation subject :")
flag = True
while True:
	if flag:
		bot1_respon = newCbSession1.Ask(subject)
		print '\033[94m' + "Bot1 : %s" %bot1_respon + '\033[0m'
		bot2_respon = newCbSession2.Ask(bot1_respon)		
		print '\033[92m' + "Bot2 : %s" %bot2_respon + '\033[0m'
		flag = False
	else:
		bot1_respon = newCbSession1.Ask(bot2_respon)
		print '\033[94m' + "Bot1 : %s" %bot1_respon + '\033[0m'
		bot2_respon = newCbSession2.Ask(bot1_respon)		
		print '\033[92m' + "Bot2 : %s" %bot2_respon + '\033[0m'


