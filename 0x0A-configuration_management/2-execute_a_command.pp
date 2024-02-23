# Kills a process named killmenow

exec { '2-execute_a_command':
    command => 'pkill killmenow',
    path    => ['/bin', '/usr/bin'],
}
