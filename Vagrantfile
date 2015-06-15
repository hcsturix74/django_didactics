Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/precise32"
  # config.vm.provision :shell, path: "install.sh"
  # config.vm.provision :shell, path: "install_not_root.sh", privileged: false
  config.vm.network :forwarded_port, host: 8000, guest: 8000
end