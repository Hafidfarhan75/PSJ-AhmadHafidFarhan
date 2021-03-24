import time
import subprocess
import threading
T1 = time.perf_counter()
hosts = ['192.168.1.1', '192.168.1.2', '192.168.1.3', '8.8.8.8', '8.8.4.4', ]
def do_something():
    status, result = subprocess.getstatusoutput("ping -c1 " + ip_host)
    if(status == 0):
        print(f'Host {ip_host} is UP')
    else:
        print(f'Host {ip_host} is DOWN')

Threads = []
for x in range(len(hosts)):
    ip_host = hosts[x]
    t = threading.Thread(target=do_something)
    t.start()
    Threads.append(t)
for th in Threads:
    th.join()
T2 = time.perf_counter()
print(f"Selesai dalam … {round(T2-T1,2)} detik")
