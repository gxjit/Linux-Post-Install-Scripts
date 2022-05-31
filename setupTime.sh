sudo apt-get install ntp

timedatectl set-timezone Asia/Kolkata

sudo ntpd -qg && sudo hwclock -w
