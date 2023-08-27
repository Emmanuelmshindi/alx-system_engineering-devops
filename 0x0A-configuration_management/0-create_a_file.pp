/* 
   Create a file in the path /tmp/school
   File permission is 0744, owner and group is www-data
   File contains I love Puppet
*/

Node default{
file{ '/tmp/school':
  ensure     => file,
  owner      => 'www-data',
  group      => 'www-data'
  mode       => '0744',
  content    => 'I love Puppet',
}
}
