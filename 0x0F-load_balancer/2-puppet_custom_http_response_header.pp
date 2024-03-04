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

exec {'cutsom header':
  command  => 'sed -i "/location \/ {/a\        add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
  provider => 'shell'
}

  service { 'nginx':
    ensure  => running,
    require => Package['nginx']
  }
