from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

# --- SYSTEM SCHEMAS ---
class HealthResponse(BaseModel):
    status: str
    database: str
    timestamp: str

class InfoResponse(BaseModel):
    app_name: str
    version: str
    environment: str
    database_type: str

# --- ITEM CRUD SCHEMAS ---
class ItemBase(BaseModel):
    title: str = Field(..., example="K3s Cluster Server")
    description: Optional[str] = Field(None, example="High Availability Control Plane Node")
    price: float = Field(0.0, example=99.99)
    is_active: bool = Field(True, example=True)

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    is_active: Optional[bool] = None

class ItemResponse(ItemBase):
    id: int
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
