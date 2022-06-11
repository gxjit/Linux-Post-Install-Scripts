
# Official 7z build 7zz(dynamically linked) or 7zzs(statically linked)
cd ~/bin && wget -qO - https://www.7-zip.org/a/7z2107-linux-x64.tar.xz |
tar -Jxf - 7zz && mv ./7zz ./7z && cd ..

# Sublime Text 3
echo "Installing Sublime Text 3 from official SublimeHQ repo"
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg\
 | sudo apt-key add -
echo "deb https://download.sublimetext.com/ apt/stable/"\
 | sudo tee /etc/apt/sources.list.d/sublime-text.list
sudo apt-get update
sudo apt-get install sublime-text

# NodeJs
echo "Installing NodeJs from NodeSource"
curl -fsSL https://deb.nodesource.com/setup_current.x | sudo -E bash -
sudo apt-get install -y nodejs
# curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
# sudo apt-get install -y nodejs



