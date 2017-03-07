from datetime import datetime
import os


class ccLogger:
    if not os.path.exists("logs"):
        os.makedirs("logs")
    bad_chars = (":", " ")
    filename = open("logs/sci-fi_game_" +
                    str(datetime.now()).replace(":", "_").replace(" ", "_")[:-7] + ".log", "w")

    def __init__(self, message):
        self.message = message
        print(message)
        raise Exception(message)

    @classmethod
    def error(cls, *args):
        log = (str(datetime.now())[:-3], " !E! ", ' '.join(args), "\n")
        ccLogger.filename.write(''.join(log))
        print(''.join(log))

    @classmethod
    def warning(cls, *args):
        log = (str(datetime.now())[:-3], " !W! ", ' '.join(args), "\n")
        ccLogger.filename.write(''.join(log))
        print(''.join(log))

    @classmethod
    def trace(cls, *args):
        log = (str(datetime.now())[:-3], " !T! ", ' '.join(args), "\n")
        ccLogger.filename.write(''.join(log))
