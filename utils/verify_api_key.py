from typing import Optional
from fastapi import HTTPException, Header
from config.settings import settings

def verify_api_key(x_api_key: Optional[str] = Header(None)):
    if x_api_key != settings.api_key:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return x_api_key
