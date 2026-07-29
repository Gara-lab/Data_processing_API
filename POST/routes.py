from fastapi import APIRouter
from schemas import TransformRequest, TransformResponse
from transformations import (
    rename_key, remove_key, copy_key, move_key, replace_value, uppercase_value, lowercase_value, 
    trim_string, merge_keys, split_key, filter_keys, sort_keys, flatten_json, 
    unflatten_json, validate_json, normalize_data
)

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

    if request.operation == "uppercase_value":
        return uppercase_value(request.data, request.key)

    if request.operation == "lowercase_value":
            return lowercase_value(request.data, request.key)

    if request.operation == "trim_string":
        return trim_string(request.data, request.key)
    
    if request.operation == "merge_keys":
        return merge_keys(request.data, request.source_keys, request.destination_key)
    
    if request.operation == "split_key":
        return split_key(request.data, request.key, request.separator)
    
    if request.operation == "filter_keys":
        return filter_keys(request.data, request.keys)
    
    if request.operation == "sort_keys":
        return sort_keys(request.data)
    
    if request.operation == "flatten_json":
        return flatten_json(request.data)
    
    if request.operation == "unflatten_json":
        return unflatten_json(request.data)
    
    if request.operation == "validate_json":
        return validate_json(request.data, request.schema)
    
    if request.operation == "normalize_data":
        return normalize_data(request.data)
    
    return rename_key(request.data, request.old_key, request.new_key)
