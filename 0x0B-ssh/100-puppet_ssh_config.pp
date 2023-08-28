#!/usr/bin/env bash
# Edit configuration file using puppet

file { 'etc/ssh/ssh_config':
         ensure => present,

content =>" 

        #SSH client configuration
	host*
	IdentityFile /alx-system_engineering-devops/0x0B-ssh/school
	PasswordAuthentication no
	",
}
