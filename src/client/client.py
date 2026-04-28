import selectors
import socket
import types

message = [b"Message 1 from client.", b"Message 2 from client."]


class Client:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 8080
        self.selector = selectors.DefaultSelector()

    def service_connection(self, key, mask):
        sock = key.fileobj
        data = key.data

        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)
            if recv_data:
                print(f"Receive from serv: {recv_data!r}")
                data.recv_total += len(recv_data)

            # NOTE: This is Temporary, just to have a condition to close connexion
            # If we received all we sent, we close
            if not recv_data or data.recv_total == data.msg_total:
                print("End of connexion")
                self.selector.unregister(sock)
                sock.close()

        if mask & selectors.EVENT_WRITE:
            # If we still have messages, we take next
            if not data.outb and data.messages:
                data.outb = data.messages.pop(0)

            if data.outb:
                print(f"Sending to serv : {data.outb!r}")
                sent = sock.send(data.outb)
                data.outb = data.outb[sent:]

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setblocking(False)
            s.connect_ex((self.host, self.port))
            events = selectors.EVENT_READ | selectors.EVENT_WRITE
            # Data has its own types and attributes
            data = types.SimpleNamespace(
                # Length of all sent messages
                msg_total=sum(len(m) for m in message),
                # Nb of received messages
                recv_total=0,
                # Copy of sent messages
                messages=message.copy(),
                outb=b"",
            )
            self.selector.register(s, events, data=data)

            try:
                # Event loop
                while data.recv_total < data.msg_total:
                    events = self.selector.select(timeout=1)
                    # If nothing, break
                    if not events:
                        break

                    for key, mask in events:
                        self.service_connection(key, mask)
            except KeyboardInterrupt:
                print("Client stopped manually")
            finally:
                self.selector.close()


if __name__ == "__main__":
    c = Client()
    c.run()
