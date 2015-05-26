#!/usr/bin/python

#from https://blogs.oracle.com/ksplice/entry/learning_by_doing_writing_your
#must run as root

#if icmp is needed: http://stackoverflow.com/questions/10256560/how-to-create-an-icmp-traceroute-in-python
#could probably update this to open one receive port and send 

import socket,time

def traceroute(dest_name):
    trace={}
    trace['ip'] = dest_name
    dest_addr = socket.gethostbyname(dest_name)
    # print 'dest_addr: ' + dest_addr
    trace['name'] = dest_addr
    port = 33435
    max_hops = 30
    icmp = socket.getprotobyname('icmp')
    udp = socket.getprotobyname('udp')
    trace['prot']='udp'
    ttl = 2
    previous_addr=""
    last_addr=dest_addr
    trace['routes']=[]
    while True:
        timer = time.clock()
        recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
        recv_socket.settimeout(1)
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)
        send_socket.settimeout(1)
        send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        recv_socket.bind(("", port))
        send_socket.sendto("", (dest_name, port))
        curr_addr = None
        curr_name = None
        try:
            _, curr_addr = recv_socket.recvfrom(0)
            print _, curr_addr
            curr_addr = curr_addr[512]
            try:
                curr_name = socket.gethostbyaddr(curr_addr)[0]
            except socket.error:
                # print socket.error
                curr_name = curr_addr
        except socket.error as msg:
            print msg
            pass
        finally:
            send_socket.close()
            recv_socket.close()

        route={}

        route['ms']=(time.clock() - timer)*1000000

        if curr_addr is not None:
            curr_host = "%s (%s)" % (curr_name, curr_addr)
            route['ip'] = curr_addr
            route['name'] = curr_name
        else:
            curr_host = "*"
        # print "%d\t%s" % (ttl, curr_host)
        
        trace['routes'].append(route)

        ttl += 1
        if curr_addr == dest_addr or ttl > max_hops or last_addr==curr_addr or last_addr==previous_addr:
            break
        previous_addr=last_addr
        last_addr=curr_addr
    return trace

print traceroute('google.com')
