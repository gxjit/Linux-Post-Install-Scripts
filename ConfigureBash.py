from subprocess import run


def main():

    aliases = {
        "ga": "git add",
        "gaa": "git add .",
        "gau": "git add --update",
        "gb": "git branch",
        "gbd": "git branch --delete ",
        "gc": "git commit",
        "gcm": "git commit --message",
        "gcf": "git commit --fixup",
        "gco": "git checkout",
        "gcob": "git checkout -b",
        "gcom": "git checkout master",
        "gcos": "git checkout staging",
        "gcod": "git checkout develop",
        "gd": "git diff",
        "gda": "git diff HEAD",
        "gi": "git init",
        "glg": "git log --graph --oneline --decorate --all",
        "gs": "git status",
        "gss": "git status --short",
        "gpo": "push origin",
        "gpom": "push origin master",
        "gplo": "pull origin",
        "gplom": "pull origin master",
        "g": "git",
        "py": "python3",
        "c": "clear",
        "n": "node",
        "ni": "npm install --save",
        "pi": "pip install",
        "ai": "sudo apt install",
        "..": "cd ..",
        "-": "cd -",
        "lsc": "ls --color=auto",
        "ll": "ls -la",
        "l.": "ls -d .* --color=auto",
    }

    env = {"PATH": "$HOME/.local/bin:$PATH"}

    with open("~/.bashrc", "a") as f:

        f.write("\n\n# Aliases\n\n")
        for name, command in aliases.items():
            f.write(f"alias {name}='{command}'\n")

        f.write("\n\n# Env Exports\n\n")
        for var, path in env.items():
            f.write(f"export {var}='{path}'\n")


if __name__ == "__main__":
    main()
