from json import loads
# from os import chdir, getcwd, mkdir
from os.path import basename, expandvars, join
# abspath, expanduser,
from pathlib import Path
from platform import system
from shutil import move, rmtree
from subprocess import DEVNULL, run
# from sys import exit, path
from tempfile import TemporaryDirectory
from urllib.request import urlopen, urlretrieve
from zipfile import ZipFile

githubFonts = ["tonsky/FiraCode", "i-tu/Hasklig"]
# "be5invis/iosevka" breaks script will fix later

googleFonts = ["Fira Mono", "Source Code Pro", "Inconsolata"]

tmp = TemporaryDirectory(ignore_cleanup_errors=True)

tmpPath = Path(tmp.name)
# print(tmp.name)
downloadPath = tmpPath.joinpath("download")
downloadPath.mkdir()
fontsPath = tmpPath.joinpath("fonts")
fontsPath.mkdir()


if system() == "Linux":
    userFonts = Path.home().joinpath(".local/share/fonts/")
    # join(expanduser("~"), ".local/share/fonts/")

elif system() == "Windows":
    userFonts = Path.home().joinpath("Downloads/fonts/")
    # join(expanduser("~"), "Downloads/fonts/")
    # userFonts = join(expandvars(r"%WINDIR%"), "Fonts/")
    # Windows install adding registry values in "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Fonts" referencing the font filename


def downloadFonts(url, fileName, downloadPath):
    zipName = f"{fileName}.zip"
    downloadFile = downloadPath.joinpath(zipName)
    # join(abspath("./download"), zipName)
    urlretrieve(url, downloadFile)
    return downloadFile


def extractFonts(downloadPath, fileName, fontsPath):
    fontsDir = fontsPath.joinpath(fileName)
    # join(abspath("./fonts"), fileName)
    with ZipFile(downloadPath) as zip:
        nameList = zip.namelist()
        for file in nameList:
            if (file.startswith("ttf/") or file.startswith("TTF/")) and file.endswith(".ttf"):
                zipInfo = zip.getinfo(file)
                zipInfo.filename = basename(file)
                zip.extract(zipInfo, fontsDir)
            elif (
                file.startswith(fileName)
                and file.endswith(".ttf")
                and "ttf/" not in nameList
            ):
                zip.extract(file, fontsDir)
            elif (
                file.startswith(fileName)
                and file.endswith(".otf")
                and "ttf/" not in nameList
            ):
                zip.extract(file, fontsDir)
    # input()
    return fontsDir


def installFonts(fontsDir, userFonts):
    installPath = userFonts.joinpath(fontsDir.name)
    # installPath = join(userFonts, basename(fontsDir))
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
    respDict = loads(urlopen(url).read().decode("utf-8"))
    downloadURL = respDict["assets"][0]["browser_download_url"]
    # if "ttc" in downloadURL:
    #     for fnt in respDict["assets"]:
    #         if "ttf" in fnt["browser_download_url"]:
    #             downloadURL = fnt["browser_download_url"]
    # else:
    #     raise()

    downloadExtractInstall(downloadURL, fileName, downloadPath, fontsPath, userFonts)


for font in githubFonts:
    downloadGithubFonts(font, downloadPath, fontsPath, userFonts)

for font in googleFonts:
    downloadGoogleFonts(font, downloadPath, fontsPath, userFonts)

if system() == "Linux":
    refreshFontCache()

# tmp.cleanup()

try:
    tmp.cleanup()
except:
    print("Unable to clean temporary directory.")

# TemporaryDirectory Bug
# def cleanUp():
#     # chdir(dd)
#     try:
#         tmp.cleanup()
#     except:
#         print("Unable to clean temporary directory.")
# import atexit
# atexit.register(cleanUp)
