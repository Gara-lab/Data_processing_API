from fastapi import APIRouter
from schemas import TransformRequest, TransformResponse
from transformations import rename_key

router = APIRouter()

@router.post("/transform", response_model=TransformResponse)
async def transform(request: TransformRequest):
    data = request.model_dump()
    return rename_key(data, "old_key", "new_key")
