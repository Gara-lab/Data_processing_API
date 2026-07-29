from pydantic import BaseModel, ConfigDict
from typing import Any, Optional

class TransformRequest(BaseModel):
    data: dict
    operation: str = "rename_key"
    old_key: Optional[str] = None
    new_key: Optional[str] = None
    key: Optional[str] = None
    source_key: Optional[str] = None
    destination_key: Optional [str] = None
    value: Optional [Any] = None
    source_keys: Optional[list[str]] = None
    separator: Optional[str] = None
    keys: Optional[list[str]] = None
    schema: Optional[dict] = None

class TransformResponse(BaseModel):
    model_config = ConfigDict(extra="allow")
