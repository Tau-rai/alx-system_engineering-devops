# makes changes to the client configuration file

file { '/home/tau_rai/.ssh/config':
    ensure  => file,
    owner   => 'ubuntu',
    group   => 'ubuntu',
    mode    => '0600',
    content => "
     Host *
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
    ",
}
