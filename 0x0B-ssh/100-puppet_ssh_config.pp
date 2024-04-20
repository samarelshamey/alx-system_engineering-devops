#!/usr/bin/env bash
#using puppet to make changes to our configuration file.
file { '/etc/ssh/ssh_config':
ensure => present,
}
file_line { 'disable pass auth':
path  => '/etc/ssh/ssh_config',
line  => 'PasswordAuthentication no',
match => 'PasswordAuthentication',
}
file_line { 'declare idenity file':
path  => '/etc/ssh/ssh_config',
line  => 'IdentityFile ~/.ssh/school',
match => 'IdentityFile',
}
