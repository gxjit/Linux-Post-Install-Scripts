# sed '/^XDG_\(PUBLIC\|MUSIC\|VIDEOS\|PICTURES\).*\"$/d' ~/.config/user-dirs.dirs

sed 's/^XDG_\(PUBLIC\|MUSIC\|VIDEOS\|PICTURES\).*\"$/# &/' ~/.config/user-dirs.dirs

echo "enabled=false" > ~/.config/user-dirs.conf

hostname "Singh-PC"
