# installs and configures a Nginx web server with puppet

class { 'nginx': }

nginx::resource::server { 'default':
  listen_port          => 80,
  www_root             => '/var/www/html',
  index_files          => ['index.html'],
  use_default_location => false,
  location_cfg_append  => {
    'return' => '301 /redirect_me',
  },
  locations            => {
    '/'            => {
      location            => '/',
      www_root            => '/var/www/html',
      index_files         => ['index.html'],
      location_cfg_append => {
        'return' => '200 "Hello World!\n"',
      },
    },
    '/redirect_me' => {
      location            => '/redirect_me',
      location_cfg_append => {
        'return' => '301 /',
      },
    },
  },
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Class['nginx'],
}
