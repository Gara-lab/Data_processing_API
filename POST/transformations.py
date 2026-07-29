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