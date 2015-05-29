__author__ = 'rjr862'
import socket, time
import EventHandler

class TCPClient(EventHandler):
    def __init__(self, sock, handler_list):
        self.sock = sock
        self.handler_list = handler_list
        self.outgoing = bytearray()

    def fileno(self):
        return self.sock.fileno()

    def send_read(self):
        if self.outgoing:
            return True
        else:
            return False

    def handle_send(self):
        nsent = self.sock.send(self.outgoing)
        self.outgoing = self.outgoing[nsent:] #save remaining bytes for later

    def handle_receive(self):
        client, addr = self.sock.accept()
        self.handler_list.append(self.client_handler(client, self.handler_list))

