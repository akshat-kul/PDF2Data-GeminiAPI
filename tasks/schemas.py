from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class TaskID(BaseModel):
    id: str = Field(None, alias="_id")  
    status: str
    result: str
    error: Optional[str]  
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        populate_by_name = True  