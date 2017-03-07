from cclogger import ccLogger


def main():
    ccLogger.error("Something went wrong")
    ccLogger.warning("There are some problems")
    ccLogger.trace("The program is running")
    logger = ccLogger("Fault")

main()
