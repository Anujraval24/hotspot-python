##simple script to create an hotspot
##author-kashyap


import sys
import subprocess

def bye():
	print("Exiting")
	sys.exit()

def hotspot():
	cmd1_output = subprocess.check_output("netsh wlan show drivers", shell=True)
	if "Hosted network supported  : Yes" in cmd1_output:
		print("Driver supported for creating a hotspot")
	host = raw_input("Name for your hotspot: ")
	password = raw_input("Enter your password (number required!!): ")
	while(len(password)<8):
		print("\n password must be at-least 8 char.long!! ")
		password = raw_input("Enter your password ")
	cmd2 = "netsh wlan set hostednetwork mode=allow ssid="+host+" key="+password
	cmd2_output = subprocess.check_output(cmd2, shell=True)
	if "successfully changed" in cmd2_output:
		print(str(host)+" created")
		cmd3_output = subprocess.check_output("netsh wlan start hostednetwork", shell=True)
		if "started" in cmd3_output:
			print(str(host)+" The hotspot is up and running")
		else:
			print("oh Crap!! (locho che kaik!!)")#native language--gujarati
			bye()
		stop = raw_input("\nPress any key to stop hotspot ")
		cmd4_output = subprocess.check_output("netsh wlan stop hostednetwork", shell=True)
		print(str(host)+"\n  has been stopped")
		print("\n Thanks for using")



