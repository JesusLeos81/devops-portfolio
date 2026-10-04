from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
import os


app = FastAPI(title="DevOps Portfolio API")


@app.get("/health")
def health():
    return {"status": "ok", "version": os.getenv("APP_VERSION", "dev")}


@app.get("/")
def root():
    return {"message": "Hola desde el pipeline DevOps"}


Instrumentator().instrument(app).expose(app)
