
Vagrant.configure("2") do |config|


  #salave_1
  config.vm.define "slave_1" do |slave_1|
    slave_1.vm.box = "bento/ubuntu-16.04"
    slave_1.vm.provider "virtualbox" do |vb|
      vb.memory = "512"
    end
    slave_1.vm.network "private_network", ip: "192.168.56.11"
    slave_1.vm.hostname = "slaveone"
    slave_1.vm.provision "shell", path: "provisioners/slave_provisioners.sh"
  end
  #slave_2
  config.vm.define "slave_2" do |slave_2|
    slave_2.vm.box = "bento/ubuntu-16.04"
    slave_2.vm.provider "virtualbox" do |vb|
      vb.memory = "512"
    end
    slave_2.vm.network "private_network", ip: "192.168.56.12"
    slave_2.vm.hostname = "slavetwo"
    slave_2.vm.provision "shell", path: "provisioners/slave_provisioners.sh"
  end
  #server
  config.vm.define "server" do |server|
    server.vm.box = "bento/ubuntu-16.04"
    server.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
    end
    server.vm.network "private_network", ip: "192.168.56.10"
    server.vm.hostname = "server"
    server.vm.provision "shell", path: "provisioners/server_provisioners.sh"
  end

end
