import sys
import subprocess

if(len(sys.argv) <= 1):
    print("Gagal: IP tujuan belum diberikan")
else:
    ip_host = sys.argv[1]
    status, result = subprocess.getstatusoutput("ping -c1 " + ip_host )
    if(status == 0):
        print(f'Host {ip_host} is UP')
    else:
        print(f'Host {ip_host} is DOWN')
