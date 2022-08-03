import mysql.connector
import socket
import json
import logging
from datetime import datetime
from pprint import pprint

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


# Utility functions
def parse_packet(packet: bytes):
    parsed_packet = {}

    packet_str = packet.decode("utf-8")
    packet_fields_raw = packet_str.split("&")
    for field in packet_fields_raw:
        packet_field = field.split(":")
        parsed_packet[packet_field[0]] = packet_field[1]

    return parsed_packet


if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Ready to listen...")
        s.bind((config["server"]["ip"], config["server"]["port"]))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(config["server"]["buffer_size"])
                if data:
                    '''
                    # parse data
                    parsed_data = parse_packet(data)
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
                    '''
                    print(data)
                    print()

