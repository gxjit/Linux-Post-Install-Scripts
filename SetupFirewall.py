from subprocess import run


def main():
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
        run(f"sudo ufw {cmd}".split(" "))


if __name__ == "__main__":
    main()

    # flatten = chain.from_iterable
    # sudoUfw = lambda cmd: run(flatten([["sudo", "ufw"], cmd]))
    # sudoUfw(cmd.split(" "))
