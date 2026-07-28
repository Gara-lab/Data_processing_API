from fastapi import APIRouter
from schemas import TransformRequest, TransformResponse

router = APIRouter()

@router.post("/transform", response_model=TransformResponse)
async def transform(request: TransformRequest):
    return request.model_dump()
