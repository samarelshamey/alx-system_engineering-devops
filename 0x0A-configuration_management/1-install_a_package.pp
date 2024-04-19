# install package flask from pip3
exec { 'installflask':
command  => '/usr/bin/pip3 install flask==2.1.0',
provider => 'shell',
returns  => [0, 1],
}
