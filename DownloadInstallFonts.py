from json import loads
from os.path import basename
from pathlib import Path
from platform import system
from shutil import move, rmtree
from subprocess import DEVNULL, run

from sys import exit
from tempfile import TemporaryDirectory
from urllib.request import urlopen, urlretrieve
from zipfile import ZipFile

githubFonts = ["tonsky/FiraCode", "i-tu/Hasklig", "JetBrains/JetBrainsMono"]

googleFonts = ["Fira Mono", "Source Code Pro", "Inconsolata"]

# Alternatives
# "arrowtype/recursive" "IBM/plex" "be5invis/Iosevka" "microsoft/cascadia-code"
# "Roboto Mono" "PT Mono" "Anonymous Pro" "Recursive" "IBM Plex Mono"
# TODO: ryanoasis/nerd-fonts support

tmp = TemporaryDirectory(ignore_cleanup_errors=True)

tmpPath = Path(tmp.name)
# print(tmp.name)
downloadPath = tmpPath.joinpath("download")
fontsPath = tmpPath.joinpath("fonts")
downloadPath.mkdir()
fontsPath.mkdir()


if system() == "Linux":
    userFonts = Path.home().joinpath(".local/share/fonts/")

elif system() == "Windows":
    userFonts = Path.home().joinpath("Downloads/fonts/")
    # userFonts = Path(expandvars(r"%WINDIR%")).joinpath("Fonts/")
    # Windows install requires adding registry values referencing the font filename
    # "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Fonts"
else:
    print("Target Unsupported.")
    exit(1)

print(f"Install location: {userFonts}")


def downloadFonts(url, fileName, downloadPath):
    zipName = f"{fileName}.zip"
    downloadFile = downloadPath.joinpath(zipName)
    urlretrieve(url, downloadFile)
    return downloadFile


def extractFonts(downloadPath, fileName, fontsPath):
    fontsDir = fontsPath.joinpath(fileName)
    with ZipFile(downloadPath) as zip:
        nameList = zip.namelist()
        for file in nameList:
            lowFile = file.lower()
            if any(
                (
                    file.startswith("_"),
                    file.startswith("."),
                    "variable" in lowFile,
                    "wght" in lowFile,
                    # "vf" in lowFile,
                )
            ):
                # print(f"skipping {file}")
                continue
            if lowFile.endswith(".ttf"):
                # print(f"extacting {file}")
                zipFileInfo = zip.getinfo(file)
                zipFileInfo.filename = basename(file)
                zip.extract(zipFileInfo, fontsDir)
    return fontsDir


def installFonts(fontsDir, userFonts):
    installPath = userFonts.joinpath(fontsDir.name)
    rmtree(installPath, ignore_errors=True)
    move(fontsDir, installPath)


def downloadExtractInstall(downloadURL, fileName, downloadPath, fontsPath, userFonts):
    print(f"Downloading {fileName}...")
    downloadFile = downloadFonts(downloadURL, fileName, downloadPath)
    print(f"Extracting {fileName}...")
    fontsDir = extractFonts(downloadFile, fileName, fontsPath)
    print(f"Installing {fileName}...")
    installFonts(fontsDir, userFonts)
    print(f"Finished! Installing {fileName}.")
    # print(tmpPath); input()


def refreshFontCache():
    print("Refreshing Fonts cache...")
    run(["fc-cache", "-fv"], shell=True, stdout=DEVNULL, stderr=DEVNULL)
    print("All Done.")


def downloadGoogleFonts(name, downloadPath, fontsPath, userFonts):
    url = f'https://fonts.google.com/download?family={name.replace(" ", "%20")}'
    fileName = name.replace(" ", "")
    downloadExtractInstall(url, fileName, downloadPath, fontsPath, userFonts)


def downloadGithubFonts(repo, downloadPath, fontsPath, userFonts):
    fileName = repo.split("/")[1]
    url = f"https://api.github.com/repos/{repo}/releases/latest"
    dwnAssets = loads(urlopen(url).read().decode("utf-8"))["assets"]

    if len(dwnAssets) == 1:
        downloadURL = dwnAssets[0]["browser_download_url"]
    else:
        for ast in dwnAssets:
            url = ast["browser_download_url"].lower()
            if "ttf" in url or "true" in url:
                downloadURL = ast["browser_download_url"]
                break

    downloadExtractInstall(downloadURL, fileName, downloadPath, fontsPath, userFonts)  # type: ignore # noqa


for font in githubFonts:
    downloadGithubFonts(font, downloadPath, fontsPath, userFonts)

for font in googleFonts:
    downloadGoogleFonts(font, downloadPath, fontsPath, userFonts)

if system() == "Linux":
    refreshFontCache()

try:  # TemporaryDirectory clean up is buggy on windows
    tmp.cleanup()
except:  # noqa
    print("Unable to clean temporary directory.")

# any(s for s in ("variable", "wght") if s in lowFile),
# "static/" in filename
