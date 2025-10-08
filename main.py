from fastapi import FastAPI
from contextlib import asynccontextmanager
from logger_config import setup_common_logger, setup_fastapi_loggers

# Настройка логирования
setup_fastapi_loggers()
logger = setup_common_logger()

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("START")
    yield
    logger.info("END")

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello World"}