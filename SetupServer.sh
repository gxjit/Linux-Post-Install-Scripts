hostname "Singh-Server"

bash $(pwd)/setupTime.sh

python3 $(pwd)/InstallUpdatePackagesServer.py -s

python3 $(pwd)/SetupFirewallServer.py -s


