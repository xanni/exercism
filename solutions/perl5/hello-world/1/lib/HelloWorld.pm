# Declare package 'HelloWorld'
package HelloWorld;

use 5.038;

use Exporter qw<import>;
our @EXPORT_OK = qw<hello>;

sub hello () {
    return 'Hello, World!';
}

1;
