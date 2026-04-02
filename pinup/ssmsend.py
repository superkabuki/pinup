import socket
import sys
from threefive import reader
from functools import partial

group = '232.0.0.1'
port = 12345
ttl = 32
DGRAM=1316
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

print(f"Sending to {group}:{port}")

with reader(sys.argv[1]) as video:
           for dgram in iter(partial(video.read, DGRAM), b""):
                sock.sendto(dgram ,(group, port))
