import json
#import os

config_data = {}

try:
    with open('configs.json','r') as f:
        config_data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError) as e:
    raise RuntimeError(f"Failed to load config: {e}")

for section, values in config_data.items():
    for key, val in values.items():
        globals()[f"{section.upper()}_{key.upper()}"] = val