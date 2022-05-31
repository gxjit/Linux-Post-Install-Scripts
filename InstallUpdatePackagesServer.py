from subprocess import run

upgrades = ["update", "upgrade"]

installs = [
    "curl",
    "xonsh",
    "glances",
    "ufw",
]

postInstalls = ["clean", "autoremove"]

for upgrade in upgrades:
    run(["sudo", "apt-get", "-y", upgrade])

for install in installs:
    run(["sudo", "apt-get", "-y", "install", install])

for postInstall in postInstalls:
    run(f"sudo apt-get -y {postInstall}")
