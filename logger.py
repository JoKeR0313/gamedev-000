from datetime import datetime
import os


class ccLogger:
    if not os.path.exists("logs"):
        os.makedirs("logs")
    filename = open("logs/sci-fi_game_" + str(datetime.now()) + ".log", "w")

    def __init__(self, message):
        self.message = message
        print(message)
        raise Exception(message)

    @classmethod
    def error(cls, message):
        log = (str(datetime.now()) + " !E! " + message + "\n")
        ccLogger.filename.write(log)
        print(log)

    @classmethod
    def warning(cls, message):
        log = (str(datetime.now()) + " !W! " + message + "\n")
        ccLogger.filename.write(log)
        print(log)

    @classmethod
    def trace(cls, message):
        log = (str(datetime.now()) + " !T! " + message + "\n")
        print(log)
