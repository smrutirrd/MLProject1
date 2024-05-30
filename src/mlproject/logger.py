import logging
import os
from datetime import datetime


#LogFile name
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#logfile path name
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
#logfolder created
os.makedirs(log_path,exist_ok=True)

#complete logfile path
LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

logging.basicConfig(filename=LOG_FILE_PATH,
    format="[%(asctime)s] -%(lineno)d -%(levelname)s-%(message)s", 
    level=logging.INFO
    )


