import os

LOG_DIR = "log"
DATA_DIR = "tmp/data"

def startup():
    os.makedirs(LOG_DIR, exist_ok=True)
    os.makedirs(DATA_DIR, exist_ok=True)