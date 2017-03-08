from cc_logger import ccLogger


def main():
    ccLogger.error("Something went wrong", 4, 3.5)
    ccLogger.warning("There are some problems", 500, 234.45)
    ccLogger.trace("The program is running", 2.345667777777777777, 45667)
    logger = ccLogger("Fault")

main()
