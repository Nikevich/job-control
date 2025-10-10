import os
import json
from datetime import date, timedelta

LOG_DIR = "log"
DATA_DIR = "tmp/data"
TEST = True

def startup():
    create_dirs()
    create_test_files()

def create_dirs():
    os.makedirs(LOG_DIR, exist_ok=True)
    os.makedirs(DATA_DIR, exist_ok=True)

def create_test_files():
    if not TEST:
        return 
    
    start_date = date(2025, 10, 1)
    days = [(start_date + timedelta(days=i)).strftime("%m.%d") for i in range(90)]

    data = {
        "users_id": "1000,1001",
        "data": [
            {
                "id": 1000,
                "fio": {
                    "name1": "Петя",
                    "family": "Петров",
                    "name2": "Петрович"
                },
                "schedule": {day: "str" for day in days}
            },
            {
                "id": 1001,
                "fio": {
                    "name1": "Иван",
                    "family": "Иванов",
                    "name2": "Иванович"
                },
                "schedule": {day: "str" for day in days}
            }
        ]
    }

    with open(os.path.join(DATA_DIR, "test.json"), "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)