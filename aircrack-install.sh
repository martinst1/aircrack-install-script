#/bin/bash
#ls -la
sudo apt-get install autoconf automake libtool shtool openssl libgcrypt11-dev pkg-config ethtool rfkill libnl-3-dev libnl-genl-3-dev libgcrypt11-dev zlib1g-dev libgcrypt20-dev libssl-dev
wget http://download.aircrack-ng.org/aircrack-ng-1.2.tar.gz
tar -zxvf aircrack-ng-1.3.tar.gz
cd aircrack-ng-1.3
autoreconf -i
./configure --with-experimental
make
sudo make install
#rm -rf aircrack-ng-1.2.tar.gz 




