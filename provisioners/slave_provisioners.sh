sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install openssh-server -y
sudo apt-get install openssh-client -y
sudo systemctl start sshd
sudo ufw enable
sudo ufw allow 22
echo "configuring ssh..."

mkdir -p /home/vagrant/.ssh
chmod 700 /home/vagrant/.ssh

touch /home/vagrant/.ssh/authorized_keys
chmod 600 /home/vagrant/.ssh/authorized_keys


echo "slave is configured."