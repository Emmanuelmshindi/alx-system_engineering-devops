/* Manifest to install a package 
   Install flask version 2.1.0 from pip3
*/

class flask_installer{
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
}
