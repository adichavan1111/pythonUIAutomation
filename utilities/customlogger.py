import logging
import os


class LogGen:
    @staticmethod
    def loggen():
        os.makedirs(".\\Logs", exist_ok=True)
        logging.basicConfig(
            filename=".\\Logs\\automation.log",
            format='%(asctime)s: %(levelname)s: %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p',
            level=logging.INFO
        )
        logger = logging.getLogger()
        return logger
