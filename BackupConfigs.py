from shutil import copy
from glob import glob
from os.path import exists, expanduser, join
from os import mkdir


def main():
    backupDest = join(expanduser("~"), "Backups")
    backupSrc = [
        ".config/sublime-text-3/Packages/User/*.sublime-build",
        ".config/sublime-text-3/Packages/User/*.sublime-settings",
        ".config/sublime-text-3/Packages/User/*.sublime-keymap",
    ]

    if not exists(backupDest):
        mkdir(backupDest)

    for path in backupSrc:
        for file in glob(join(expanduser("~"), path)):
            copy(file, backupDest)
            print(f'\nCopying :\n{file}\nto:\n{backupDest}')


if __name__ == "__main__":
    main()
