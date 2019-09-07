npmdir="${HOME}/.npm-packages"
mkdir ${npmdir}
npm config set prefix $npmdir
sudo chown -R `whoami` $npmdir

# export PATH="${npmdir}/bin:$PATH" # checkout ConfigureBash.py
