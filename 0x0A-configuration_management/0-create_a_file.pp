# Create a file named school inside the tmp folder
file { '/tmp/school':
  ensure   => file,
  owner    => 'www-data',
  group    => 'www-data',
  mode     => '0744',
  content  => 'I love Puppet',
}
