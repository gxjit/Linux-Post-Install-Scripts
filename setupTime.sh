sudo apt-get install ntp

sudo timedatectl set-timezone Asia/Kolkata

sudo ntpd -qg && sudo hwclock -w
