sudo hostname "Singh-PC"
bash $(pwd)/setupTime.sh
bash $(pwd)/ConfigureGit.sh
python3 $(pwd)/ConfigureBash.py
python3 $(pwd)/InstallUpdatePackages.py
bash $(pwd)/InstallSnaps.sh
bash $(pwd)/InstallThirdParty.sh
python3 $(pwd)/TweakGnome.py
python3 $(pwd)/SetupFirewall.py
python3 $(pwd)/DownloadInstallFonts.py
# bash $(pwd)/npmConfig.sh