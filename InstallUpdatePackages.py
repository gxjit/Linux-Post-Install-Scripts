from subprocess import run


def main():

    upgrades = ["update", "upgrade"]

    installs = [
        "build-essential",
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

    snaps = ["code", "chromium"]

    postInstalls = ["install --fix-broken", "autoremove"]

    for upgrade in upgrades:
        run(["sudo", "apt", "--yes", upgrade])

    for install in installs:
        run(["sudo", "apt", "--yes", "install", install])

    for postInstall in postInstalls:
        run(f"sudo apt --yes {postInstall}".split(" "))

    for snap in snaps:
        run(["sudo", "snap", "install", snap])


if __name__ == "__main__":
    main()
