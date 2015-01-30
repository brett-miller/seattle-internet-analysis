#!/usr/bin/python

#from https://blogs.oracle.com/ksplice/entry/learning_by_doing_writing_your
#must run as root

#if icmp is needed: http://stackoverflow.com/questions/10256560/how-to-create-an-icmp-traceroute-in-python
#could probably update this to open one receive port and send 

import socket

def main(dest_name):
    dest_addr = socket.gethostbyname(dest_name)
    print 'dest_addr: ' + dest_addr
    port = 33434
    max_hops = 30
    icmp = socket.getprotobyname('icmp')
    udp = socket.getprotobyname('udp')
    ttl = 2
    last_addr=dest_addr
    while True:
        recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
        # recv_socket.settimeout(1)
        # send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
        send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        recv_socket.bind(("", port))
        send_socket.sendto("", (dest_name, port))
        curr_addr = None
        curr_name = None
        try:
            _, curr_addr = recv_socket.recvfrom(512)
            # print _, curr_addr
            curr_addr = curr_addr[0]
            try:
                curr_name = socket.gethostbyaddr(curr_addr)[0]
            except socket.error:
                # print socket.error
                curr_name = curr_addr
        except socket.error:
            # print socket.error
            pass
        finally:
            send_socket.close()
            recv_socket.close()

        if curr_addr is not None:
            curr_host = "%s (%s)" % (curr_name, curr_addr)
        else:
            curr_host = "*"
        print "%d\t%s" % (ttl, curr_host)

        ttl += 1
        if curr_addr == dest_addr or ttl > max_hops or last_addr==curr_addr:
            break
        last_addr=curr_addr

if __name__ == "__main__":
    main('google.com')