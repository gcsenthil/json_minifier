import json
import base64
import uuid

def generate_short_id():
    unique_id = str(uuid.uuid4())
    base64_encoded_id = base64.b64encode(unique_id.encode()).decode()[:8]
    return base64_encoded_id

def replace_ids(data, count_dict):
    if isinstance(data, dict):
        updated_dict = {}
        for key, value in data.items():
            if key not in count_dict:
                count_dict[key] = generate_short_id()
            new_key = count_dict[key]
            new_value = replace_ids(value, count_dict)
            updated_dict[new_key] = new_value
        return updated_dict
    elif isinstance(data, list):
        return [replace_ids(item, count_dict) for item in data]
    else:
        return data

def restore_keys(data, count_dict):
    if isinstance(data, dict):
        restored_dict = {}
        for key, value in data.items():
            original_key = next((k for k, v in count_dict.items() if v == key), key)
            restored_key = restore_keys(original_key, count_dict)
            restored_value = restore_keys(value, count_dict)
            restored_dict[restored_key] = restored_value
        return restored_dict
    elif isinstance(data, list):
        return [restore_keys(item, count_dict) for item in data]
    else:
        return data

def convert_to_minified_json(json_data, count_dict):
    data = json.loads(json_data)
    updated_data = replace_ids(data, count_dict)
    minified_json = json.dumps(updated_data)
    return minified_json

def revert_to_original_json(minified_json, count_dict):
    updated_data = json.loads(minified_json)
    restored_data = restore_keys(updated_data, count_dict)
    original_json = json.dumps(restored_data, indent=2)
    return original_json

# Example usage
json_data = """
  {"person": {"name": "John Doe", "age": 30, "address": {"city": "New York", "zipcode": "10001"}, "contacts": [{"type": "email", "value": "john.doe@example.com"}, {"type": "phone", "value": "123-456-7890"}]}}
"""

# Convert to minified JSON
count_dict = {}
minified_json = convert_to_minified_json(json_data, count_dict)
print('Minified JSON:\n', minified_json)

# Revert back to original JSON
original_json = revert_to_original_json(minified_json, count_dict)
print('\nOriginal JSON:\n', original_json)
