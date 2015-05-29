__author__ = 'rjr862'
import TCPClient, TCPServer

class TCPEchoClient(TCPClient):

    def receive_ready(self):
        True

    def handle_receive(self):
        data = self.sock.recv(8192)
        if not data:
            self.close()
        else:
            self.outgoing.extend(data)


if __name__ == '__main__':
    handlers = []
    handlers.append(TCPServer(('16000'), TCPEchoClient, handlers))
    event_loop(handlers)