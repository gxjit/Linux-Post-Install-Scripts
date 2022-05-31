sudo apt-get install ntp

sudo timedatectl set-timezone Asia/Kolkata

sudo timedatectl set-local-rtc 1

sudo ntpd -qg && sudo hwclock -w

sudo systemctl disable systemd-timesyncd --now