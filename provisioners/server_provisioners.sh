sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install sshpass -y
sudo apt-get install openssh-server -y
sudo apt-get install openssh-client -y
sudo systemctl start sshd
sudo ufw enable
sudo ufw allow 22


echo "configuring SSH server and generating key..."
sudo su
ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa <<< $'\n'
echo "copying key to slaveone"
sshpass -p "vagrant" ssh-copy-id -o StrictHostKeyChecking=no vagrant@192.168.56.11
echo "copying key to slavetwo"
sshpass -p "vagrant" ssh-copy-id -o StrictHostKeyChecking=no vagrant@192.168.56.12

echo "server is ready."