from subprocess import run, PIPE


def main():

    getProfile = run(
        ["gsettings", "get", "org.gnome.Terminal.ProfilesList", "default"],
        check=True,
        stdout=PIPE,
    )
    terminalProfile = getProfile.stdout.decode().replace("'", "").strip()

    settings = [
        "shell.extensions.dash-to-dock show-apps-at-top true",
        "shell.extensions.dash-to-dock click-action 'minimize'",
        "shell.extensions.dash-to-dock dock-fixed false",
        "desktop.interface gtk-theme 'Adwaita-dark'",
        "desktop.interface clock-show-date true",
        "desktop.interface clock-format 12h",
        "desktop.wm.preferences button-layout 'close,minimize,maximize:'",
        "settings-daemon.plugins.color night-light-enabled true",
        "settings-daemon.plugins.color night-light-schedule-automatic true",
        "shell.extensions.dash-to-dock dock-fixed false",
        "desktop.privacy remove-old-trash-files true",
        "desktop.privacy remove-old-temp-files true",
        "desktop.privacy old-files-age 14",
        "settings-daemon.plugins.power sleep-inactive-ac-type 'suspend'",
        "Terminal.Legacy.Settings theme-variant 'dark'",
        "gedit.preferences.editor scheme 'tango'",
        "settings-daemon.plugins.power sleep-inactive-ac-timeout 900",
        "desktop.peripherals.mouse speed 0.49",
        "gedit.preferences.editor editor-font 'Fira Mono Medium 22'",
        (
            "Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:"
            f"{terminalProfile}/ use-system-font false"
        ),
        (
            "Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:"
            f"{terminalProfile}/ font 'Fira Mono Medium 22'"
        ),
    ]

    for setting in settings:
        run(f"gsettings set org.gnome.{setting}".split(" ", maxsplit=4))


if __name__ == "__main__":
    main()

