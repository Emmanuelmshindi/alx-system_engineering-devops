/*
  Manifest that kills the process killmenow
  Must use exec resource and pkill
*/

exec { 'killmenow':
  command => 'pkill killmenow',
}
