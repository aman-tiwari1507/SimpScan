from socket import gethostbyname
import pyfiglet
from termcolor import cprint
import os
import nmap3

colors="255;0;255:"
colors1="255;255;100:"

def PingScan():
	pyfiglet.print_figlet("__________", font="standard", colors=colors1)
	cprint('[+] Do You want to enter IP or URL [ip/url] ------> ','red',attrs=['bold'],end=' ')
	res = input()
	print()
	if(res=='ip' or res=='IP' or res=='Ip'):
		cprint('[+] Input the IP to be Checked ------> ','red',attrs=['bold'],end=' ')
		ip = input()
		print()
	else:	
		cprint('[+] Input the URL to be Checked ------> ','red',attrs=['bold'],end=' ')
		url = input()
		ip = gethostbyname(url)
		print()
	cprint('[+] No of Packets to Be Sent ------> ','red',attrs=['bold'],end=' ')
	n=input()
	print()
	os.system(f'ping -c {n} {ip} > files/ping.txt')
	os.system('cat files/ping.txt | tail -2 | head -1')
	print()
	f=open('files/ping.txt','r')
	a=f.readlines()
	f.close()
	b=a[-2]
	c=b.split()
	if(c[3]=='0'):
		cprint('[+]   The System is Not Live   [+]','red',attrs=['bold']) 
	else:
		cprint('[+]   The System is Live   [+]','red',attrs=['bold'])
	
def Trace():
	pyfiglet.print_figlet("__________", font="standard", colors=colors1)
	cprint('[+] Do You want to enter IP or URL [ip/url] ------> ','red',attrs=['bold'],end=' ')
	res = input()
	print()
	if(res=='ip' or res=='IP' or res=='Ip'):
		cprint('[+] Input the IP to be Checked ------> ','red',attrs=['bold'],end=' ')
		ip = input()
		print()
	else:	
		cprint('[+] Input the URL to be Checked ------> ','red',attrs=['bold'],end=' ')
		url = input()
		ip = gethostbyname(url)
		print()
	os.system(f'traceroute {ip} > files/trace.txt')
	f=open('files/trace.txt','r')
	a=f.readlines()
	f.close()
	b=len(a) - 1
	cprint(f'[+] The No of Hops ------> {b} ','red',attrs=['bold'],end=' ')
	
def OpPorts():
	pyfiglet.print_figlet("__________", font="standard", colors=colors1)
	cprint('[+] Input the IP or URL to be Checked ------> ','red',attrs=['bold'],end=' ')
	res=input()
	print()
	nmap = nmap3.NmapHostDiscovery()
	results = nmap.nmap_portscan_only(res)
	for i in results[res]:
		cprint(f'[+] {i["service"]["name"]}({i["portid"]}) : {i["state"].upper()} [+]','green',attrs=['bold'])
		print()

def OsScan():
	pyfiglet.print_figlet("__________", font="standard", colors=colors1)
	cprint('[+] Input the IP or URL to be Checked ------> ','red',attrs=['bold'],end=' ')
	res=input()
	print()
	nmap = nmap3.Nmap()
	results = nmap.nmap_version_detection(res)
	for i in results:
		try:
			cprint(f'[+] ({i["port"]}) : {i["service"]["product"]} : {i["service"]["version"]} : {i["service"]["extrainfo"]} [+]','red',attrs=['bold'])
			print()
		except KeyError as e:
			a=str(e)
			cprint(f'[+] ({i["port"]}) : {i["service"]["product"]} : {a.upper()} Couldnt Be Detected [+]','red',attrs=['bold'])
			print()
	
pyfiglet.print_figlet("SimpScan!!", font="standard", colors=colors)
print("[+][+]  { A Simple Network Scanner For Beginners }   [+][+]",end=" ")
n=0
while(n<=4):
	pyfiglet.print_figlet("__________", font="standard", colors=colors1)
	cprint('[1] ------> Check If IP is Live','red',attrs=['bold'])
	print()
	cprint('[2] ------> Number of Hops to IP','red',attrs=['bold'])
	print()
	cprint('[3] ------> Open Ports of IP','red',attrs=['bold'])
	print()
	cprint('[4] ------> OS Detection for The IP','red',attrs=['bold'])
	print()
	cprint('[5] ------> Exit','red',attrs=['bold'])
	print()
	cprint('[+] Input Your Choice ------> ','red',attrs=['bold'],end=' ')
	n = int(input())
	if(n==1):
		PingScan()
	if(n==2):
		Trace()
	if(n==3):
		pyfiglet.print_figlet("__________", font="standard", colors=colors1)
		cprint('[+] Would You First Like To Check If The System is Live [+] [y/n] { SUGGESTED }-------> ','red',attrs=['bold'], end=' ')
		a=input()
		if(a=='y' or a=='Y'):
			PingScan()
			pyfiglet.print_figlet("__________", font="standard", colors=colors1)
			cprint('[+] Would You Like To Check For Open Ports (If System is Live) [+] [y/n]-------> ','red',attrs=['bold'], end=' ')
			b=input()
			if(b=='y' or b=='Y'):
				OpPorts()
		else:
			OpPorts()
	if(n==4):
		pyfiglet.print_figlet("__________", font="standard", colors=colors1)
		cprint('[+] Would You First Like To Check If The System is Live [+] [y/n] { SUGGESTED }-------> ','red',attrs=['bold'], end=' ')
		a=input()
		if(a=='y' or a=='Y'):
			PingScan()
			pyfiglet.print_figlet("__________", font="standard", colors=colors1)
			cprint('[+] Would You Like To Detect The Operating System (If System is Live) [+] [y/n]-------> ','red',attrs=['bold'], end=' ')
			b=input()
			if(b=='y' or b=='Y'):
				OsScan()
		else:
			OsScan()
		

