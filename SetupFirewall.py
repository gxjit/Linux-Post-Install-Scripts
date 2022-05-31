from subprocess import run


cmds = [
    "reset",
    "status",
    "default deny incoming",
    "default deny outgoing",
    "allow out http",
    "allow out https",
    "allow out ssh",
    "allow out dns",
    "logging off", # Minimize writes to SSD
    "enable",
    "status",
]

for cmd in cmds:
    run(f"sudo ufw {cmd}")
