IRC is used by Electrum Dash server to find 'peers' - other Electrum Dash servers. The
current list can be seen by running:

  electrum-dash-server peers

The following config file options are used by the IRC part of Electrum Dash server:

    [server]
    irc = yes
    irc_nick = server_nickname
    host = fqdn.host.name.tld
    # report_host = fqdn.host.name.tld
    # report_stratum_tcp_port = 50001

`irc` is used to determine whether the IRC thread will be started or
the Electrum Dash server will run in private mode (default). In private
mode, `electrum-dash-server peers` will always return an empty list.

`host` is a fully-qualified domain name (FQDN) of your Electrum Dash
server. It is used both when binding the listener for incoming client
connections and as part of the realname field in IRC (see below).

`report_host` is a an optional fully-qualified domain name (FQDN) of
your Electrum Dash server instead of `host`. It is used as part of the name
field in IRC for incoming client connections.  This is useful in a NAT
setup where you bind to a private IP locally but have an external IP
set up at your router and external DNS.

`report_stratum_tcp_port` and `report_stratum_tcp_ssl_port` are
optional settings for a port number to be reported in the IRC name
field without actually binding this port locally. This is useful in a
NAT setup where you might want to bind to a high port locally but DNAT
a different possibly privileged port for inbound connections

`irc_nick` is a nick name that will be appended to the D_ suffix when
composing the IRC nickname to identify your server on #electrum-dash .

Please note the IRC name field can only contain 50 chars and will be
composed of `host` + protocol version number + Port numbers for the
various protocols.  Please check whether port numbers are cut off at
the end


Example of port forwarding using iptables:
iptables -t nat -A PREROUTING -p tcp --dport 110 -j REDIRECT --to-ports 50002

