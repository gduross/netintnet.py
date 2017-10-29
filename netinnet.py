#
#
# The purpose of this script is to determine if on subnet falls within another subnet.
# Example : Is 192.168.0.32/27 within 192.168.1.0/24 ? Answer : No
#
# The format to use this script is : python netinnet.py 192.168.0.32/27 192.168.1.0/24
#
# Started 7/29/2017
# Version V.01
#
# status: working
#
# NOTE: This script uses the ipaddress module which might not be a part of the standard library.
#

# Imports:
import sys
import ipaddress

# The function:
def netinnet(var01,var02):
        ips1 = [ipaddress.ip_address(ip) for ip in ipaddress.ip_network(var01.decode("ascii"))]
        ips2 = [ipaddress.ip_address(ip) for ip in ipaddress.ip_network(var02.decode("ascii"))]

        if min(ips1)>=min(ips2) and max(ips1)<=max(ips2):
                var03 = "yes"
        else:
                var03 = "no"

        print "\nIs "+var01+ " within " +var02 +" ? "+var03+"\n"

# Run the function and pass in the variables:
netinnet(sys.argv[1],sys.argv[2])
