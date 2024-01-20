# json_minifier
JSON Minifier is a Python script that provides a simple way to minify and restore JSON data using unique short identifiers. The script replaces JSON keys with compact and reversible identifiers, reducing the size of the JSON data.
#Features
Minification: Converts JSON data into a minified format with short and unique identifiers.
Restoration: Reverts minified JSON back to its original structure.
Customizable IDs: Allows customization of the identifier generation method (e.g., using UUIDs, base64 encoding).
Reusability: The script is designed to be reusable and easily integrated into different projects.
Usage
Minification:

Pass your JSON data to convert_to_minified_json(json_data, count_dict).
Retrieve the minified JSON data.
Restoration:

Pass the minified JSON data and the count dictionary to revert_to_original_json(minified_json, count_dict).
Retrieve the original JSON data.

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

License
This project is licensed under the MIT License.
