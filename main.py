from fastapi import FastAPI
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager
from logger_config import setup_common_logger, setup_fastapi_loggers
from startup import startup

startup()

# Настройка логирования
setup_fastapi_loggers()
logger = setup_common_logger()

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("START")
    yield
    logger.info("END")

app = FastAPI(lifespan=lifespan)

@app.get("/test/")
async def test_short():
    file_path = "tmp/data/test.json"
    return FileResponse(path=file_path, media_type="application/jdon", filename="test.json")