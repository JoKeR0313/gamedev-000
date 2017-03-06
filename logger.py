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
    def error(cls, *args):
        log = (str(datetime.now()), " !E! ", ' '.join(args), "\n")
        ccLogger.filename.write(''.join(log))
        print(log)

    @classmethod
    def warning(cls, *args):
        log = (str(datetime.now()), " !W! ", ' '.join(args), "\n")
        ccLogger.filename.write(''.join(log))
        print(log)

    @classmethod
    def trace(cls, *args):
        log = (str(datetime.now()), " !T! ", ' '.join(args), "\n")
        print(log)

ccLogger.error("Error", "Missing")
ccLogger.warning("Warning", "Not have")
ccLogger.trace("Trace", "Program is running")
