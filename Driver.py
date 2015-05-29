__author__ = 'rjr862'
import select

def event_loop(handlers):
    while True:
        recv_rdy = [h for h in handlers if h.receive_ready]
        snd_rdy = [h for h in handlers if h.send_ready]
        can_recv , can_send, _ = select.select(recv_rdy, snd_rdy, [])
        for h in can_recv:
            h.handle_receive()
        for h in can_send:
            h.handle_send()