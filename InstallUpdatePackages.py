from argparse import ArgumentParser
from subprocess import run


def parseArgs():
    parser = ArgumentParser()
    parser.add_argument("-s", "--server", action="store_true")

    return parser.parse_args()


pargs = parseArgs()

upgrades = ["update", "upgrade"]

commonInstalls = ["ufw", "python-is-python3", "xonsh", "curl"]

if not pargs.server:

    installs = [
        *commonInstalls,
        "build-essential",
        "synaptic",
        "gnome-tweaks",
        "vlc",
        "gparted",
        # "yt-dlp",
    ]

elif pargs.server:

    installs = [
        *commonInstalls,
        "glances",
    ]


postInstalls = ["autoremove", "clean"]

# run = print # test

for upgrade in upgrades:
    run(["sudo", "apt-get", "-y", upgrade])

for install in installs:
    run(["sudo", "apt-get", "-y", "install", install])

for postInstall in postInstalls:
    run(f"sudo apt-get -y {postInstall}")
