import logging
from logging.handlers import TimedRotatingFileHandler
import os
from datetime import datetime

def _create_rotating_handler(log_prefix: str) -> TimedRotatingFileHandler:
    """
    Формат файла: log/{log_prefix}-YYYY-MM-DD.log
    """
    LOG_DIR = "log"
    os.makedirs(LOG_DIR, exist_ok=True)

    current_date = datetime.now().strftime("%Y-%m-%d")
    log_file = os.path.join(LOG_DIR, f"{log_prefix}-{current_date}.log")

    handler = TimedRotatingFileHandler(
        log_file, when="midnight", interval=1, backupCount=7, encoding="utf-8"
    )
    handler.suffix = "%Y-%m-%d"
    handler.setFormatter(logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    ))

    return handler


def setup_common_logger() -> logging.Logger:
    """
    Логгер для пользовательских сообщений приложения.
    """
    logger = logging.getLogger("app_common")
    logger.setLevel(logging.INFO)

    # очищаем старые хендлеры, если есть
    logger.handlers.clear()
    logger.addHandler(_create_rotating_handler("app-common"))
    logger.propagate = False
    return logger


def setup_fastapi_loggers():
    """
    Перенастраивает встроенные логгеры FastAPI и Uvicorn
    для вывода только в файл log/app-fastapi-YYYY-MM-DD.log.
    """
    fastapi_handler = _create_rotating_handler("app-fastapi")

    for name in ("uvicorn", "uvicorn.error", "uvicorn.access", "fastapi"):
        log = logging.getLogger(name)
        log.handlers.clear()
        log.addHandler(fastapi_handler)
        log.setLevel(logging.INFO)
        log.propagate = False