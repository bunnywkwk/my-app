from fastapi import FastAPI
from app.config import settings
from app.database import engine, Base
from app.routers import system, items

# Auto-create tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="Production-grade DevOps FastAPI application with PostgreSQL connection and CRUD support.",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Register application routers
app.include_router(system.router)
app.include_router(items.router)

@app.get("/", summary="Root Endpoint")
def read_root():
    return {
        "message": f"Welcome to {settings.APP_NAME}!",
        "environment": settings.ENVIRONMENT,
        "docs": "/docs",
        "health": "/health",
        "info": "/info"
    }
