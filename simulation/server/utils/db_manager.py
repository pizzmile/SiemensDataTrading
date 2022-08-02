import mysql.connector
import logging


logger = logging.getLogger(__name__)


class DBManager:

    def __init__(self, host: str, user: str, password: str, database: str):
        self.__db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.__cursor = self.__db.cursor()

        logger.debug("Created connector to DB")

    def get_device_id(self, dev_name: str):
        sql = "SELECT idDevice FROM SS_DB.devices WHERE name = %s"
        var = (dev_name,)
        self.__cursor.execute(sql, var)
        result = self.__cursor.fetchone()
        return result[0]

    def insert_processed_work(self, timestamp: str, duration: str, defective: str, success: str, id_device: str):
        sql = "INSERT INTO SS_DB.works (timestamp, duration, defective, success, idDevice) " \
              "VALUES (%s, %s, %s, %s, %s)"
        var = (timestamp, duration, defective, success, id_device,)
        self.__cursor.execute(sql, var)
        self.__db.commit()

        logger.debug(f"Written data to DB: {var}")
