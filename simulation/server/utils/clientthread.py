import logging
from threading import Thread


logger = logging.getLogger(__name__)


class ClientThread(Thread):

    def __init__(self, ip, port, conn):
        Thread.__init__()

        self.ip = ip
        self.port = port
        self.conn = conn

        logger.info(f"[+] New thread started for {ip}:{port}")

    def run(self):
        are_data_present = True

        while are_data_present:
            data = self.conn.recv(2048)

            if not data:
                are_data_present = False
            else:
                logger.info(f"Received data: /n/t{data}")
                self.conn.send(b"ACK")