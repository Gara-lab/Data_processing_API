from fastapi import APIRouter
from schemas import TransformRequest, TransformResponse
from transformations import rename_key

router = APIRouter()

@router.post("/transform", response_model=TransformResponse)
async def transform(request: TransformRequest):
    return {
        "data": rename_key(request.data, request.old_key, request.new_key)
    }
