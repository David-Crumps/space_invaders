import json
import os
from typing import Any


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..'))
CONFIG_PATH = os.path.join(PROJECT_ROOT, 'configs.json')
STUB_PATH = os.path.join(PROJECT_ROOT, 'src' ,'configs.pyi')

def infer_type(value: Any) -> str:
    if isinstance(value, bool):
        return 'bool'
    elif isinstance(value, int):
        return 'int'
    elif isinstance(value, float):
        return 'float'
    elif isinstance(value, str):
        return 'str'
    elif isinstance(value, list):
        if not value:
            return 'list[Any]'
        inner_type = infer_type(value[0])
        return f'list[{inner_type}]'
    elif isinstance(value, dict):
        return 'dict[str, Any]'
    else:
        return 'Any'
    
def flatten_config(data: dict, prefix: str='') -> dict:
    flat = {}
    for key, value in data.items():
        full_key = f"{prefix}_{key}" if prefix else key
        if isinstance(value, dict):
            flat.update(flatten_config(value, full_key))
        else:
            flat[full_key.upper()] = value
    return flat

def generate_stub():
    try:
        with open('configs.json','r') as f:
         config_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Failed to load config: {e}")
    
    flat_config = flatten_config(config_data)
    with open(STUB_PATH, 'w') as stub:
        for key, value in flat_config.items():
            type_hint = infer_type(value)
            stub.write(f"{key}: {type_hint}\n")
    print(f"Stub file generated: {STUB_PATH}")

if __name__ == "__main__":
    generate_stub()