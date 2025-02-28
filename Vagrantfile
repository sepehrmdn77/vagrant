Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-24.04"
  config.vm.box_version = "202502.21.0"
  config.vm.network "forwarded_port", guest: 22, host: 2222, id: "ssh"

  #salave_1
  config.vm.define "slave_1" do |slave_1|
    slave_1.vm.box = "bento/ubuntu-24.04"
      config.vm.box_version = "202502.21.0"
    slave_1.vm.provider "virtualbox" do |vb|
      vb.memory = "512"
    end
    slave_1.vm.network "private_network", ip: "192.168.56.11"
    slave_1.vm.hostname = "slave1"
    slave_1.vm.provision "shell", path: "provisioners/slave_provisioners.sh"
    slave_1.vm.network "forwarded_port", guest: 22, host: 2223, id: "ssh_slave_1"
  end
  #slave_2
  config.vm.define "slave_2" do |slave_2|
    slave_2.vm.box = "bento/ubuntu-24.04"
      config.vm.box_version = "202502.21.0"
    slave_2.vm.provider "virtualbox" do |vb|
      vb.memory = "512"
    end
    slave_2.vm.network "private_network", ip: "192.168.56.12"
    slave_2.vm.hostname = "slave2"
    slave_2.vm.provision "shell", path: "provisioners/slave_provisioners.sh"
    slave_2.vm.network "forwarded_port", guest: 22, host: 2224, id: "ssh_slave_2"
  end
  #server
  config.vm.define "server" do |server|
    server.vm.box = "bento/ubuntu-24.04"
      config.vm.box_version = "202502.21.0"
    server.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
    end
    server.vm.network "private_network", ip: "192.168.56.10"
    server.vm.hostname = "server"
    server.vm.provision "shell", path: "provisioners/server_provisioners.sh"
    server.vm.network "forwarded_port", guest: 22, host: 2225, id: "ssh_server"
  end

end