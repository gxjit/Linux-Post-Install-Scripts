from argparse import ArgumentParser
from subprocess import run


def parseArgs():
    parser = ArgumentParser()
    parser.add_argument("-s", "--server", action="store_true")

    return parser.parse_args()


pargs = parseArgs()

upgrades = ["update", "upgrade"]

if not pargs.server:

    installs = [
        "build-essential",
        "python-is-python3",
        "curl",
        "xclip",
        "synaptic",
        "gnome-tweaks",
        "ufw",
        "vlc",
        "gparted",
        "ffmpeg",
        # "youtube-dl",
    ]

elif pargs.server:

    installs = [
        "curl",
        "python-is-python3",
        "xonsh",
        "glances",
        "ufw",
    ]


postInstalls = ["autoremove", "clean"]

for upgrade in upgrades:
    run(["sudo", "apt-get", "-y", upgrade])

for install in installs:
    run(["sudo", "apt-get", "-y", "install", install])

for postInstall in postInstalls:
    run(f"sudo apt-get -y {postInstall}")
