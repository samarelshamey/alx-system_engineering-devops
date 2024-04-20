#using puppet to make changes to config file
file { '/etc/ssh/ssh_config':
content => "
HostName 18.210.19.143
User ubuntu
IdentityFile ~/.ssh/school
PasswordAuthentication no",
}
