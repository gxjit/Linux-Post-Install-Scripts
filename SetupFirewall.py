from subprocess import run


cmds = [
    "reset",
    "status",
    "default deny incoming",
    "default deny outgoing",
    "allow out http",
    "allow out https",
    "allow out 53",
    "allow out 22",
    "logging on",
    "enable",
    "status",
]

for cmd in cmds:
    run(f"sudo ufw {cmd}")
