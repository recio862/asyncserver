__author__ = 'rjr862'

class EventHandler:

    def fileno(self):
        pass

    def receive_ready(self):
        return False

    def handle_receive(self):
        pass

    def send_ready(self):
        return False

    def handle_send(self):
        pass