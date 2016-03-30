from host import bye,hotspot
import sys,subprocess

def home():
	print ("Let me check for admin status")
	try:
		output = subprocess.check_output("whoami /groups | find \"S-1-16-12288\"", shell=True)
	except:
		print("You are not an admin :( ")
		bye()
	if('S-1-16-12288' in output):
		print("Good you are an admin")
		hotspot()
		
if __name__ == '__main__':
	home()
