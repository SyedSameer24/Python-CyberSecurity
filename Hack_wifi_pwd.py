import subprocess, re

w = lambda cmd: subprocess.run(cmd, capture_output=True, text=True).stdout
profiles = re.findall(r"All User Profile\s*:\s*(.*)", w(["netsh","wlan","show","profiles"]))

for p in profiles:
    p = p.strip()
    info = w(["netsh","wlan","show","profile",p,"key=clear"])
    pwd = re.search(r"Key Content\s*:\s*(.*)", info)
    print(f"{p} : {pwd.group(1) if pwd else 'OPEN/NO PASSWORD'}")
