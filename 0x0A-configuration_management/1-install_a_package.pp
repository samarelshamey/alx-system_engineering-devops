# A puppet manifest installing flask from pip3.
# specifying the version of flask 
package { 'flask':
ensure   => 2.1.0,
provider => pip3,
}
