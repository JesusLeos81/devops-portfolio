from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
import os

app = FastAPI(title="DevOps Portfolio API")

# Endpoint de salud: Kubernetes lo usará para saber si el pod está vivo
@app.get("/health")
def health():
    return {"status": "ok", "version": os.getenv("APP_VERSION", "dev")}

@app.get("/")
def root():
    return {"message": "Hola desde el pipeline DevOps"}

# Expone métricas en /metrics para que Prometheus las recolecte
Instrumentator().instrument(app).expose(app);