from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import text
from datetime import datetime
from app.database import get_db
from app.config import settings
from app.schemas import HealthResponse, InfoResponse

router = APIRouter(tags=["System & Monitoring"])

@router.get("/health", response_model=HealthResponse, summary="Liveness & Readiness Health Probe")
def get_health(db: Session = Depends(get_db)):
    """
    Kubernetes Liveness and Readiness Probe Endpoint.
    Executes a simple database ping ('SELECT 1') to verify connectivity.
    """
    try:
        db.execute(text("SELECT 1"))
        db_status = "connected"
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database connection error: {str(e)}"
        )

    return {
        "status": "healthy",
        "database": db_status,
        "timestamp": datetime.utcnow().isoformat()
    }

@router.get("/info", response_model=InfoResponse, summary="Application Runtime Info")
def get_info():
    """
    Returns environment, application version, and database type.
    Used by GitOps & developers to verify which deployment environment (staging/prod) is running.
    """
    db_type = "PostgreSQL" if "postgresql" in settings.database_url else "SQLite"
    return {
        "app_name": settings.APP_NAME,
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
        "database_type": db_type
    }
