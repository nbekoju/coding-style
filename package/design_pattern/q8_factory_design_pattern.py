# [Factory Design Pattern] Build a logging system using the Factory Design Pattern. Create a LoggerFactory class that generates different types of loggers (e.g., FileLogger, ConsoleLogger, DatabaseLogger). Implement methods in each logger to write logs to their respective destinations. Show how the Factory Design Pattern helps to decouple the logging system from the application and allows for flexible log handling.

from abc import ABC, abstractmethod
import datetime
import sqlite3
import csv


class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass


class FileLogger(Logger):
    def __init__(self):
        super().__init__()
        print("creating the file logger object")

    def log(self, message):
        timestamp = str(datetime.datetime.now())
        with open("log_file.txt", "a") as file:
            file.write(timestamp + "\t" + message + "\n")


class ConsoleLogger(Logger):
    def __init__(self):
        super().__init__()
        print("creating the console logger object")

    def log(self, message):
        timestamp = str(datetime.datetime.now())
        print(timestamp + "\t" + message)


class CSVLogger(Logger):
    def __init__(self):
        super().__init__()
        print("creating the CSV logger object")

    def log(self, message):
        timestamp = str(datetime.datetime.now())
        log_entry = {"timestamp": timestamp, "message": message}
        with open("log.csv", "a", newline="") as csvfile:
            fieldnames = ["timestamp", "message"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(log_entry)


class DatabaseLogger(Logger):
    def __init__(self) -> None:
        super().__init__()
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        self.connection = sqlite3.connect("log_database.db")
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS logs
                            (id INTEGER PRIMARY KEY,
                            message TEXT,
                            timestamp TIMESTAMP)"""
        )
        self.connection.commit()

    def log(self, message):
        timestamp = datetime.datetime.now()
        self.cursor.execute(
            "INSERT INTO logs (message, timestamp) VALUES (?, ?)", (message, timestamp)
        )
        self.connection.commit()

    def close(self):
        self.connection.close()


class LoggerFactory:
    def get_logger(self, logger_type):
        if logger_type == "file":
            return FileLogger()
        elif logger_type == "console":
            return ConsoleLogger()
        elif logger_type == "csv":
            return CSVLogger()
        elif logger_type == "database":
            return DatabaseLogger()
        else:
            raise ValueError("Invalid Logger type")


if __name__ == "__main__":
    logger_type_list = ["file", "console", "csv", "database"]
    logger_type = logger_type_list[2]

    logger_factory = LoggerFactory()
    logger = logger_factory.get_logger(logger_type)

    logger.log("This is 4 log message.")
