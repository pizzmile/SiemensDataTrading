import mysql.connector
import socket
import json
from pprint import pprint

# Load configuration from file
with open('./config.json', 'r') as f:
    config = json.load(f)

mydb = mysql.connector.connect(
    host=config["database"]["host"],
    user=config["database"]["user"],
    password=config["database"]["password"]
)
mycursor = mydb.cursor()


# Utility functions
def parse_packet(packet: bytes):
    parsed_packet = {}

    packet_str = packet.decode("utf-8")
    packet_fields_raw = packet_str.split("&")
    for field in packet_fields_raw:
        packet_field = field.split(":")
        parsed_packet[packet_field[0]] = packet_field[1]

    return parsed_packet


def get_device_id(dev_name: str):
    sql = "SELECT idDevice FROM SS_DB.device WHERE name = %s"
    var = (dev_name,)
    mycursor.execute(sql, var)
    result = mycursor.fetchone()
    return result[0]


def insert_processed_work(timestamp: int, duration: int, defective: int, success: int, id_device: int):
    sql = "INSERT INTO SS_DB.processedWork (timestamp, duration, defective, success, idDevice) " \
          "VALUES (%d, %d, %d, %d, %d)"
    var = (timestamp, duration, defective, success, id_device,)
    mycursor.execute(sql, var)
    mydb.commit()


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
                    parsed_data = parse_packet(data)
                    dev_id = get_device_id(parsed_data["devName"])
                    insert_processed_work(
                        int(data["timestamp"]),
                        int(data["duration"]),
                        int(data["defective"]),
                        int(data["success"]),
                        dev_id)
                    print(parsed_data)

