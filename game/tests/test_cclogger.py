import import_dir_setter
from cc_logger import ccLogger


def test_cclogger():
    ccLogger.trace("Starting in ..")
    for counter in range(5, -1, -1):
        ccLogger.trace("..", counter, "..")

    ccLogger.error("Sample: Something went wrong", 4, 3.5)
    ccLogger.warning("Sample: There are some problems", 500, 234.45)
    ccLogger.trace("The program is running", 2.345667777777777777, 45667)
    try:
        logger = ccLogger("Logger can't be intantiated and this is intended.")
    except:
        pass
    ccLogger.trace("Exiting..")

if '__main__' == __name__:
    test_cclogger()
