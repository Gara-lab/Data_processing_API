from fastapi import APIRouter
from schemas import TransformRequest, TransformResponse
from transformations import rename_key, remove_key, copy_key, move_key, replace_value

router = APIRouter()

@router.post("/transform", response_model=TransformResponse)
async def transform(request: TransformRequest):
    if request.operation == "remove_key":
        return remove_key(request.data, request.key)

    if request.operation == "copy_key":
        return copy_key(request.data, request.source_key, request.destination_key)
    
    if request.operation == "move_key":
        return move_key(request.data, request.source_key, request.destination_key)

    if request.operation == "replace_value":
        return replace_value(request.data, request.key, request.value)
    
    return rename_key(request.data, request.old_key, request.new_key)
    
