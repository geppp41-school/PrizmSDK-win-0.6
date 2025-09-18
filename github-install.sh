sudo dpkg --add-architecture i386 ##
sudo apt update
sudo apt install -y libc6-dev:i386 gcc-multilib g++-multilib xserver-xorg-dev:i386 libfreetype6-dev:i386 flex 
sudo apt install -y wine