import socket
import struct
from threefive import Stream

GRP = '232.0.0.1'  # SSM range
SRC = '127.0.0.1' # Specific Source IP
PORT = 12345

IP_ADD_ENUM=39  # Windows may be 17?

ANY_LOCAL='0.0.0.0'
DATAGRAM=1316

def func(cue):
    """
    func func to call when we find a SCTE-35 Cue
    """
    cue.show()


def mk_sock():
    """
    mk_sock make an SSM Multicast socket
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((GRP, PORT))
    if not hasattr(socket, "IP_ADD_SOURCE_MEMBERSHIP"):
        setattr(socket, "IP_ADD_SOURCE_MEMBERSHIP", IP_ADD_ENUM)
    mreq = struct.pack('4s4s4s', socket.inet_aton(GRP), socket.inet_aton(SRC), socket.inet_aton(ANY_LOCAL))
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_SOURCE_MEMBERSHIP, mreq)
    print(f"Listening for SSM stream {SRC} -> {GRP}:{PORT}")
    return sock


def read_ssm():
    """
    read_ssm read datagrams from SSM stream
    and pass them to a threefive Stream instance
    for parsing.
    """
    sock=mk_sock()
    strm=Stream(None)
    while True:
        datagram, addr = sock.recvfrom(DATAGRAM)
        strm._decode2cues(datagram, func)

if __name__=='__main__':
    read_ssm()
