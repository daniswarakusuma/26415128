#! /usr/bin/perl -s

use strict;
use warnings;

my $filename = 'danis.txt';
open(my $fh, '<:encoding(UTF-8)', $filename)
 or die "Gak bisa dibukak filenya '$filename' $!";

while (my $row = <$fh>) {
 chomp $row;
 print "$row\n";
}
