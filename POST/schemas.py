from pydantic import BaseModel, ConfigDict

class TransformRequest(BaseModel):
    data: dict
    old_key: str
    new_key: str

class TransformResponse(BaseModel):
    data: dict
