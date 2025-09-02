import logging
import os
from pathlib import Path


class Loggen:
    @staticmethod
    def get_logger():
        # project_root = Path(__file__).parent.parent
        # logs_dir = project_root/"logs"
        # logs_dir.mkdir(exist_ok=True)
        # logs_file = logs_dir/f"{file_name}.log"
        # print(f"attempting to log to :{logs_file}")

        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)



        logging.basicConfig(filename= r"C:\Users\nikhi\PycharmProjects\framework1\logs\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I :%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        print(f"logger_created")
        return logger



