
echo "Installing Sublime Text 3 from official SublimeHQ repo"
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg\
 | sudo apt-key add -
echo "deb https://download.sublimetext.com/ apt/stable/"\
 | sudo tee /etc/apt/sources.list.d/sublime-text.list
sudo apt-get update
sudo apt-get install sublime-text

echo "Installing NodeJs from NodeSource"
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
sudo apt-get install -y nodejs