import select
import socket
import logging
from utils import ClientThread

logger = logging.getLogger(__name__)
logging.basicConfig(filename="log.log", encoding="utf-8", level=logging.DEBUG)


TCP_IP = "0.0.0.0"
TCP_PORT = 62
BUFFER_SIZE = 1024

threads = []
keep_alive = True   # condition to keep the server alive


if __name__ == '__main__':
    # Setup
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(('', 6200))
        logger.debug(f"Socket successfully created")
        server_socket.listen(10)
    except socket.error as err:
        logger.error("socket creation failed with error %s" % err)

    read_sockets, write_sockets, error_sockets = select.select([server_socket], [], [])

    # Main
    while keep_alive:
        logger.info("Waiting for incoming connections...")

        for sock in read_sockets:
            (conn, (ip, port)) = server_socket.accept()
            new_thread = ClientThread(ip, port, conn)
            new_thread.start()
            threads.append(new_thread)

        for t in threads:
            t.join()
