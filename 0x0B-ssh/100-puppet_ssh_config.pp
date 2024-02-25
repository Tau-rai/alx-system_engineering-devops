# makes changes to the client configuration file

file_line { 'Password Authentication':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   =>  'PasswordAuthentication no',
}

file_line { 'Identity file':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school',
}
