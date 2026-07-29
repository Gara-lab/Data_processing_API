def rename_key(data, old_key, new_key):
    if old_key in data:
        data[new_key] = data.pop(old_key)
    return data

def remove_key(data, key):
    if key in data:
        data.pop(key)
    return data

def copy_key(data, source_key, destination_key):
    if source_key in data:
        data[destination_key] = data[source_key]
    return data

def move_key(data, source_key, destination_key):
    if source_key in data:
        copy_key(data, source_key, destination_key)
        remove_key(data, source_key)
    return data

def replace_value(data, key, value):
    if key in data:
        data[key] = value
    return data

def uppercase_value(data, key):
    if key in data and isinstance(data[key], str):
        data[key] = data[key].upper()
    return data

def lowercase_value(data, key):
    if key in data and isinstance(data[key], str):
        data[key] = data[key].lower()
    return data

def trim_string(data, key):
    if key in data and isinstance(data[key], str):
        data[key] = data[key].strip()
    return data

def merge_keys(data, source_keys, destination_key):
    merged_values = [data[k] for k in source_keys if k in data]
    if merged_values:
        data[destination_key] = merged_values
    for k in source_keys:
        data.pop(k, None)
    return data

def split_key(data, key, separator):
    if key in data and isinstance(data[key], str):
        data[key] = data[key].split(separator)
    return data

def filter_keys(data, keys):
    return {k: data[k] for k in keys if k in data}

def sort_keys(data):
    return dict(sorted(data.items()))

def flatten_json(data, parent_key='', sep='_'):
    items = {}
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_json(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items

def unflatten_json(data, sep='_'):
    result = {}
    for k, v in data.items():
        parts = k.split(sep)
        d = result
        for part in parts[:-1]:
            if part not in d:
                d[part] = {}
            d = d[part]
        d[parts[-1]] = v
    return result

def validate_json(data, schema):
    errors = []
    type_map = {"str": str, "int": int, "float": float, "bool": bool, "list": list, "dict": dict}
    for k, expected_type in schema.items():
        if k not in data:
            errors.append(f"Missing key: {k}")
        elif expected_type in type_map and not isinstance(data[k], type_map[expected_type]):
            errors.append(f"Invalid type for {k}: expected {expected_type}")
    return {"valid": len(errors) == 0, "errors": errors}

def normalize_data(data):
    normalized = {}
    for k, v in data.items():
        if isinstance(v, str):
            normalized[k] = v.lower().strip()
        else:
            normalized[k] = v
    return normalized