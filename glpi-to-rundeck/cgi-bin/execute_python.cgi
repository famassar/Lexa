#!/usr/bin/perl

use strict;
use warnings;
use CGI;

my $cgi = CGI->new;

print $cgi->header('text/html');

my $param1 = $cgi->param('param1');
my $param2 = $cgi->param('param2');
my $param3 = $cgi->param('param3');
my $param4 = $cgi->param('param4');

if (defined $param1 && defined $param2 && defined $param3 && defined $param4) {
    my $output = `/usr/bin/python3 /opt/lexa/glpi-to-rundeck/glpi-to-rundeck.py \-o $param1 \-v $param2 \-s $param3 \-u $param4 2>&1`;
    print "<pre>$output</pre>";
} else {
    print "Error: Missing parameters";
}
