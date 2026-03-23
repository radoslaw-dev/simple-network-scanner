import subprocess
import time

base = input("Enter the IP base: (e.g. 192.168.0.) ")
start = int(input("Enter the IP starting range: (e.g. 1) "))
end = int(input("Enter the IP ending range: (e.g. 20) "))

active = []
start_time= time.time()
for i in range(start, end+1):
    ip = base + str(i)
    print(f"Scanning {ip}..." )
    final = subprocess.run(["ping", "-n", "1", ip], shell=False, stdout=subprocess.DEVNULL)
    if final.returncode == 0:
        print(f"[+] {ip} is active")
        active.append(ip)
    else:
        print(f"[-] {ip} is inactive")
end_time = time.time()

print("======== Scan complete ========")
print(f"Active hosts: {len(active)}")
print(f"Time elapsed: {round((end_time - start_time), 2)} seconds")

for element in active:
    print(f"[+] {element}")
