
sudo apt-get install systemd-timesyncd

confFile="/etc/systemd/timesyncd.conf"

echo -e "NTP=0.pool.ntp.org\nFallbackNTP=time.cloudflare.com" \
 | sudo tee -a ${confFile}

# echo "PollIntervalMinSec=900,PollIntervalMaxSec=3600" \
#  | sudo tee -a ${confFile}

cat ${confFile}

sudo systemctl restart systemd-timesyncd

sudo timedatectl set-ntp true

sudo timedatectl set-timezone Asia/Kolkata

timedatectl status

timedatectl timesync-status

# sudo systemctl disable systemd-timesyncd --now
# sudo apt-get install ntp
# sudo ntpd -qg && sudo hwclock -w