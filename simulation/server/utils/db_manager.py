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

    def insert_processed_work(self, timestamp: str, idDevice: str, current: str, voltage: str, activePower: str, reactivePower: str, apparentPower: str):
        sql = "INSERT INTO SS_DB.energyConsumptions (timestamp, idDevice, current, voltage, activePower, reactivePower, apparentPower)"
        var = (timestamp, idDevice, current, voltage, activePower, reactivePower, apparentPower,)
        self.__cursor.execute(sql, var)
        self.__db.commit()

        logger.debug(f"Written data to DB: {var}")
