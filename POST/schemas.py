from pydantic import BaseModel, ConfigDict

class TransformRequest(BaseModel):
    model_config = ConfigDict(extra="allow")

class TransformResponse(BaseModel):
    data: dict
