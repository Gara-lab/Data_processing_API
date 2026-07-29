from pydantic import BaseModel, ConfigDict
from typing import Optional

class TransformRequest(BaseModel):
    data: dict
    operation: str = "rename_key"
    old_key: Optional[str] = None
    new_key: Optional[str] = None
    key: Optional[str] = None

class TransformResponse(BaseModel):
    data: dict
