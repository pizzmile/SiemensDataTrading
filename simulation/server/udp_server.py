import mysql.connector
import socket
import json
import logging
from _thread import *
from datetime import datetime

from utils import DBManager


def parse_packet(packet: bytes):
    parsed_packet = {}

    packet_str = packet.decode("utf-8")
    packet_fields_raw = packet_str.split("&")
    for field in packet_fields_raw:
        packet_field = field.split(":")
        parsed_packet[packet_field[0]] = packet_field[1]

    return parsed_packet


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

        if message:
            # parse data
            parsed_data = parse_packet(message)
            dev_id = dbmanager.get_device_id(parsed_data["devName"])

            # log
            logger.debug(f"Received message: {parsed_data}")
            print(parsed_data)

            # get current timestamp
            timestamp_format = '%Y-%m-%d %H:%M:%S'
            timestamp = datetime.now().strftime(timestamp_format)
            # write to db
            dbmanager.insert_processed_work(
                timestamp,
                str(dev_id),
                parsed_data["current"],
                parsed_data["voltage"],
                parsed_data["activePower"],
                parsed_data["reactivePower"],
                parsed_data["apparentPower"]
            )
