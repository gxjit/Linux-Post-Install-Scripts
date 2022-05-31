from subprocess import run


cmds = [
    "reset",
    "status",
    "default deny incoming",
    "default deny outgoing",
    "allow out ssh", # 22
    "allow out http", # 80
    "allow out https", # 443
    "allow out dns", # 53
    "allow in ssh",
    # "allow in 2222/tcp",
    # "allow in 53/udp"
    # "allow in http",
    # "allow in https",
    "logging off", # Minimize writes to SSD
    "enable",
    "status",
]

for cmd in cmds:
    run(f"sudo ufw {cmd}")
