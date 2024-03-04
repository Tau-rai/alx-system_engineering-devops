# This manifest installs and configures Nginx server with a custom header

exec { 'update system':
        command => '/usr/bin/apt-get update',
}

package { 'nginx':
    ensure  => 'installed',
    require => Exec['update system']
}

file {'/var/www/html/index.html':
  content => 'Hello World!'
}

$hostname = $facts['networking']['fqdn']

file_line { 'nginx_custom_header':
  path  => '/etc/nginx/sites-available/default',
  line  => "        add_header X-Served-By ${hostname};",
  match => '^        location / {$',
  after => '^        location / {$',
}

exec { 'test_nginx_config':
  command     => 'nginx -t',
  refreshonly => true,
  subscribe   => File_line['nginx_custom_header'],
}

  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => Exec['test_nginx_config'],
  }
