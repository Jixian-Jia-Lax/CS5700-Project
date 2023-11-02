'''
https://man7.org/linux/man-pages/man7/raw.7.html
'''


import socket
import struct 

# make IP header
def makeIPHeader(srcIP,desIP,length,frag_off):

    # ip header fields
    ip_ver = 4
    ip_ihl = 5
    ip_tos = 0
    ip_tot_len = length	# kernel will fill the correct total length
    ip_id = 54321	#Id of this packet
    ip_frag_off = frag_off
    ip_ttl = 255
    ip_proto = socket.IPPROTO_RAW
    ip_check = 0	# kernel will fill the correct checksum
    ip_saddr = socket.inet_aton ( srcIP )	
    ip_daddr = socket.inet_aton ( desIP )

    ip_ihl_ver = (ip_ver << 4) + ip_ihl

    # the ! in the pack format string means network order
    ip_header = struct.pack('!BBHHHBBH4s4s' , ip_ihl_ver, ip_tos, ip_tot_len, ip_id, ip_frag_off, ip_ttl, ip_proto, ip_check, ip_saddr, ip_daddr)
    return ip_header


def makeUDPHeader(srcPort,desPort,length,):
    





serverPort = 12000
serverSocket = socket(socket.AF_INET, socket.SOCK_RAW,socket.IPPROTO_RAW)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')
while True: 
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(),clientAddress)