from subprocess import run


cmds = [
    "reset",
    "status",
    "default deny incoming",
    "default deny outgoing",
    "allow out ssh",
    "allow out http",
    "allow out https",
    "allow out 53", # DNS
    "allow in ssh",
    "allow in 2222",
    # "allow in http",
    # "allow in https",
    "logging off", # Minimize writes to SSD
    "enable",
    "status",
]

for cmd in cmds:
    run(f"sudo ufw {cmd}")
