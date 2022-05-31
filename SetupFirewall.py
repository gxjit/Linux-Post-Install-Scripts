from argparse import ArgumentParser
from subprocess import run


def parseArgs():
    parser = ArgumentParser()
    parser.add_argument("-s", "--server", action="store_true")

    return parser.parse_args()


pargs = parseArgs()

cmds = [
    "reset",
    "status",
    "logging off",  # Minimize writes to SSD
    "default deny incoming",
    "default deny outgoing",
    "allow out dns",  # 53
    "allow out ssh",  # 22
    "allow out http",  # 80
    "allow out https",  # 443
]

if pargs.server:

    cmds = [
        *cmds,
        "allow in ssh",
        # "allow in 2222/tcp",
        # "allow in 53/udp"
        # "allow in http",
        # "allow in https",
    ]

cmds = [*cmds, "enable", "status"]


for cmd in cmds:
    run(f"sudo ufw {cmd}")
    # run(f"echo ufw {cmd}")
