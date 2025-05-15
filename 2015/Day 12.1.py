import json, re

def is_int(value) -> bool:
    return bool(re.match(r"^[+-]?[0-9]+$", value))
    
def run_dict(JSON_dict: dict) -> int:
    counter = 0
    for key in JSON_dict.keys():
        value = JSON_dict[key]
        if isinstance(value, int):
            counter += value
        elif isinstance(value, dict):
            counter += run_dict(value)
        elif isinstance(value, list):
            counter += run_list(value)
    return counter
        
def run_list(JSON_list: list) -> int:
    counter = 0
    for value in JSON_list:    
        if isinstance(value, int):
            counter += value
        elif isinstance(value, dict):
            counter += run_dict(value)
        elif isinstance(value, list):
            counter += run_list(value)
    return counter

def main():
    print("Input:")
    JSON_obj = json.loads(input())
    
    print(f"Sum of all numbers: {run_dict(JSON_obj)}")

if __name__ == "__main__":
    main()
