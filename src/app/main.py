from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import uvicorn
import time
import os

app = FastAPI(title="DevSecOps Microservice", version="1.0.0")


@app.get("/health")
def health_check():
    return {"status": "ok", "timestamp": time.time()}


@app.get("/info")
def service_info():
    return {
        "service": "DevSecOps Microservice",
        "version": "1.0.0",
        "hostname": os.getenv("HOSTNAME", "unknown")
    }


@app.get("/metrics", response_class=PlainTextResponse)
def metrics():
    return "app_requests_total 1\napp_uptime_seconds 123"


if name == "main":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
