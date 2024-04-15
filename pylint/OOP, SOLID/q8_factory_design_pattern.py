"""
Build a logging system using the Factory Design Pattern. 
Create a LoggerFactory class that generates different types of 
loggers (e.g., FileLogger, ConsoleLogger, DatabaseLogger). 
Implement methods in each logger to write logs to their respective destinations. 
Show how the Factory Design Pattern helps to decouple the 
logging system from the application and allows for flexible log handling.
"""

from abc import ABC, abstractmethod
import datetime
import sqlite3
import csv


class Logger(ABC):
    """logger abstract class"""
    @abstractmethod
    def log(self, message):
        """log message"""


class FileLogger(Logger):
    """file logger subclass"""
    def __init__(self):
        super().__init__()
        print("creating the file logger object")

    def log(self, message):
        """log the message to the log file"""
        timestamp = str(datetime.datetime.now())
        with open("log_file.txt", "a", encoding="utf-8") as file:
            file.write(timestamp + "\t" + message + "\n")


class ConsoleLogger(Logger):
    """console logger subclasss"""
    def __init__(self):
        super().__init__()
        print("creating the console logger object")

    def log(self, message):
        """log the message to the console"""
        timestamp = str(datetime.datetime.now())
        print(timestamp + "\t" + message)


class CSVLogger(Logger):
    """csv logger subclass"""
    def __init__(self):
        super().__init__()
        print("creating the CSV logger object")

    def log(self, message):
        """log message to the csv file"""
        timestamp = str(datetime.datetime.now())
        log_entry = {"timestamp": timestamp, "message": message}
        with open("log.csv", "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["timestamp", "message"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(log_entry)


class DatabaseLogger(Logger):
    """database logger subclass"""
    def __init__(self) -> None:
        super().__init__()
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        """connect tot he database"""
        self.connection = sqlite3.connect("log_database.db")
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """create table if not exists"""
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS logs
                            (id INTEGER PRIMARY KEY,
                            message TEXT,
                            timestamp TIMESTAMP)"""
        )
        self.connection.commit()

    def log(self, message):
        """log the message to the database"""
        timestamp = datetime.datetime.now()
        self.cursor.execute(
            "INSERT INTO logs (message, timestamp) VALUES (?, ?)", (message, timestamp)
        )
        self.connection.commit()

    def close(self):
        """close the database connection"""
        self.connection.close()


class LoggerFactory:
    """return different logger as per the logger type"""
    def get_logger(self, logger):
        """get logger on the basis of logger type"""
        if logger == "file":
            return FileLogger()
        if logger == "console":
            return ConsoleLogger()
        if logger == "csv":
            return CSVLogger()
        if logger == "database":
            return DatabaseLogger()
        raise ValueError("Invalid Logger type")


if __name__ == "__main__":
    logger_type_list = ["file", "console", "csv", "database"]
    LOGGER_TYPE = logger_type_list[2]

    logger_factory = LoggerFactory()
    logger_object = logger_factory.get_logger(LOGGER_TYPE)

    logger_object.log("This is 4 log message.")
