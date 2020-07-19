import os
import platform
import threading
from datetime import datetime

ip_alive=[]
netwokr_scan=''
command_os=''

def scan_ip(start,end):
	for num in range(start,end):
		ip=netwokr_scan+str(num)
		cmd=command_os+ip
		result=os.popen(cmd)
		for line in result.readlines():
			if("TTL" in line):
				ip_alive.append(ip)
				break

class MyThread(threading.Thread):
	def __init__(self,start_ip,end_ip):
		threading.Thread.__init__(self)
		self.start_ip=start_ip
		self.end_ip=end_ip
	def run(self):
		scan_ip(self.start_ip,self.end_ip)


net_addr=input('Input network address subnet need to test: ')
net_lst=net_addr.split('.')
netwokr_scan=net_lst[0]+'.'+net_lst[1]+'.'+net_lst[2]+'.'
start_num=int(input('Input start number: '))
end_num=int(input('Input end number: '))
os_sys=platform.system()
if(os_sys=='Windows'):
	command_os='ping -n 1 '
	print('Current System is Window!!!')
else:	
	command_os='ping -c 1 '
	print('Current System is Linux/Unix!!!')

t1=datetime.now()
num_ip=end_num - start_num
ip_per_thread=20
total_thread=int(num_ip/ip_per_thread +1)
threads=[]
try:
	for i in range(total_thread):
		end=start_num+ip_per_thread
		if (end>end_num):
			end=end_num
		thread=MyThread(start_num,end)
		thread.start()
		threads.append(thread)
		start_num=end
except Exception as e:
	print(e)

print("Number thread active: {}".format(threading.activeCount()))
for a_thread in threads:
	a_thread.join()

for a_ip in ip_alive:
	print("IP {} is online now!!!".format(a_ip))
t2=datetime.now()

print("Scanning IP complete with total time: {}".format(t2-t1))