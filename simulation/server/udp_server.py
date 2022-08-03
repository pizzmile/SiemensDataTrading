import mysql.connector
import socket
import json
import logging
from _thread import *
from datetime import datetime

from utils import DBManager

logger = logging.getLogger(__name__)
logging.basicConfig(filename="log.log", level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s - %(message)s', datefmt='%H:%M:%S')


# Load configuration from file
with open('./config.json', 'r') as f:
    config = json.load(f)

dbmanager = DBManager(
    host=config["database"]["host"],
    user=config["database"]["user"],
    password=config["database"]["password"],
    database=config["database"]["database"]
)

if __name__ == '__main__':
    UDP_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDP_socket.bind((config["server"]["ip"], config["server"]["port"]))
    print("UDP server up and listening...")

    while True:
        byte_address_pair = UDP_socket.recvfrom(config["server"]["buffer_size"])
        message = byte_address_pair[0]
        address = byte_address_pair[1]
        print(f"Message from {address}: {message}")
